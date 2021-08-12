from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD


def keyboard(lang_code):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.top_referrals,
                    callback_data=menu_profile_cd.new(command=MenuProfileCD.show_top_referral)
                )
            ]
        ]
    )
    return markup
