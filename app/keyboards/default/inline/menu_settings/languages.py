from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.settings_profile import choice_lang_cd
from app.loader import config
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_lang_code


def keyboard(user: User) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    for lang in config.bot.languages:

        if user.lang_code == lang:
            continue

        markup.insert(
            InlineKeyboardButton(
                text=format_lang_code(lang),
                callback_data=choice_lang_cd.new(user_id=user.id, lang_code=lang)
            )
        )
    return markup
