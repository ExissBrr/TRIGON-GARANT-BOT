from aiogram.dispatcher.handler import CancelHandler

import app
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update, ChatType, Message

from app.data import text
from app.data.types.user_data import UserCaptchaText
from app.utils.bot.languages import get_lang_code
from app.utils.captcha.image_captcha import CaptchaImage
from app.utils.captcha.tools import generate_random_text
from app.utils.db_api.models.user import User


class FloodDefenderMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: Update, *args):
        obj = update.message or update.callback_query or update.inline_query

        if not ChatType.is_private(obj):
            return False



        user_from_telegram = obj.from_user
        user: User = await User.get(user_from_telegram.id)

        if not user:
            return False

        if isinstance(obj, Message) and user.captcha_text != UserCaptchaText.NONE:

            if obj.text and CaptchaImage.check_answer(user.captcha_text, obj.text):
                await user.update(captcha_text=UserCaptchaText.NONE)
                return await obj.answer('✅')
        elif user.captcha_text != UserCaptchaText.NONE:
            raise CancelHandler()

        if not app.loader.is_flood_defender:
            return False

        captcha_text = generate_random_text()

        captcha_photo = CaptchaImage(captcha_text)

        lang_code = get_lang_code()

        await obj.bot.send_photo(
            chat_id=user.id,
            photo=captcha_photo.input_file,
            caption=text[lang_code].default.message.flood_defender_captcha_text(
                captcha_text=captcha_text
            )
        )
        await user.update(captcha_text=captcha_text)