from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD


def make_keyboard(lang_code):
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.change_details,
            callback_data=menu_profile_cd.new(command=MenuProfileCD.change_requisites)
        )
    )
    return markup
