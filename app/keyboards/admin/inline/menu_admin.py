from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.data import text
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice


def make_keyboard_admin_menu(lang_code):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_sending_messages,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SEND_MESSAGES)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_statistic,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SHOW_STATISTIC)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_settings_bot,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SHOW_BOT_SETTINGS)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_add_scam,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.ADD_SCAMMER)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_scam_list,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SHOW_SCAM_LIST)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_controversy_deals,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SHOW_CONTROVERSY_DEALS)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_payments,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.PAYMENTS)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_seller,
            callback_data=admin_menu_cd.new(command=AdminMenuChoice.SHOW_SELLER_MENU)
        )
    )
    return markup
