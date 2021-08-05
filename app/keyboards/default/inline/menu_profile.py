from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD


def keyboard(lang_code):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.top_up_balance,
                    callback_data=menu_profile_cd.new(command=MenuProfileCD.top_up_balance)
                ),
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.withdraw_balance,
                    callback_data=menu_profile_cd.new(command=MenuProfileCD.withdraw_balance)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.my_bargains,

                    callback_data=menu_profile_cd.new(command=MenuProfileCD.show_menu_deals)
                ),
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.requisites,
                    callback_data=menu_profile_cd.new(command=MenuProfileCD.menu_requisites)
                )
            ]
        ]
    )
    return markup
