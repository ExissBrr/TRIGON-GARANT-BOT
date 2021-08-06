from aiogram.types import Message

from app.loader import dp
from app import keyboards
from app.data import text
from app.data.text.ru.button.reply import show_menu_sellers


@dp.message_handler(reply_command=show_menu_sellers)
async def show_menu_category(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=keyboards.default.inline.sellers.show_menu.make_keyboard_seller_requests(lang_code)
    )
