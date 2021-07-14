from aiogram.types import Message, ContentTypes
from loguru import logger

from app.loader import dp
from app.data import text
from app.filters.private.user.is_read_rules import NotReadRules
from app.keyboards.default import reply
from app.keyboards.default.inline import generator_button_url
from app.loader import config, links
from app.states.private.registration_new_user import RegistrationNewUser
from app.utils.format_data.user import format_lang_code


@dp.message_handler(NotReadRules(), state='*', content_types=ContentTypes.ANY)
@dp.message_handler(state=RegistrationNewUser.choice_language)
async def message_on(message: Message, user, lang_code):
    for lang in config.bot.languages:
        if message.text == format_lang_code(lang):
            await user.update_data(lang_code=lang)
            lang_code = lang

    await message.answer_video(
        video=links.video.read_rules,
        caption=text[lang_code].default.message.please_read_the_rules,
        reply_markup=reply.agree_rules.keyboard(lang_code)
    )

    links_data = {
        text[lang_code].default.button.inline.bot_rules: links.telegraph.bot_rules,
    }

    await message.answer(
        text=text[lang_code].default.message.links_to_rules,
        reply_markup=generator_button_url.keyboard(links_data)
    )
    await RegistrationNewUser.agree_rules.set()
