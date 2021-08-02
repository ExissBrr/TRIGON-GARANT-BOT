from symbol import return_stmt
from time import sleep

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update, ChatType, Message
from loguru import logger

import app
from app.data import text
from app.data.types.user_data import UserCaptchaText
from app.loader import flood_user_in_processing, flood_timeout
from app.utils.bot.languages import get_lang_code
from app.utils.captcha.image_captcha import CaptchaImage
from app.utils.captcha.tools import generate_random_text
from app.utils.db_api.models.user import User


class FloodDefenderMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: Update, *args):
        obj = update.message or update.callback_query or update.inline_query
        if not obj.chat.type == ChatType.PRIVATE:
            return CancelHandler

        user_from_telegram = obj.from_user
        user: User = await User.get(user_from_telegram.id)

        if not user:
            return False

        if isinstance(obj, Message) and user.captcha_text != UserCaptchaText.NONE:

            if obj.text and CaptchaImage.check_answer(user.captcha_text, obj.text):
                await user.update_data(captcha_text=UserCaptchaText.NONE)
                try:
                    await obj.answer('✅')
                except:
                    pass
                raise CancelHandler


        if user.captcha_text != UserCaptchaText.NONE:
            raise CancelHandler

        if not app.loader.is_flood_defender:
            return False

        if user.id in flood_user_in_processing:
            raise CancelHandler
        else:
            flood_user_in_processing.append(user.id)

        captcha_text = generate_random_text()

        captcha_photo = CaptchaImage(captcha_text)

        lang_code = await get_lang_code()

        try:
            await obj.bot.send_photo(
                chat_id=user.id,
                photo=captcha_photo.input_file,
                caption=text[lang_code].default.message.flood_defender_captcha_text.format(flood_timeout=flood_timeout)
            )
        except:
            raise CancelHandler

        if user.captcha_text != UserCaptchaText.NONE:
            raise CancelHandler

        await user.update_data(captcha_text=captcha_text)
        raise CancelHandler
