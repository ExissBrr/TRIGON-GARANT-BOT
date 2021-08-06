from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].button.reply.search_users)
            ],
            [
                KeyboardButton(text[lang_code].button.reply.profile)
            ],
            [
                KeyboardButton(
                    text=text[lang_code].button.reply.show_menu_sellers
                ),
                KeyboardButton(
                    text=text[lang_code].button.reply.search_scam
                )
            ],
            [
                KeyboardButton(text[lang_code].button.reply.menu_help)
            ]
        ]
    )
    return markup
