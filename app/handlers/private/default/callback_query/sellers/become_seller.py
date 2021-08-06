from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers
from app.loader import dp
from app.states.private.become_to_seller import BecomeToSeller


@dp.callback_query_handler(sellers_cd.filter(command=CommandsSellers.become_seller))
async def choice_category(call: CallbackQuery, lang_code):
    await call.answer(text='One moment..', cache_time=5)
    await call.message.answer(
        text=text[lang_code].default.message.choose_your_seller_category,
        reply_markup=keyboards.default.reply.sellers.category_list.make_keyboard_scam_category_list(lang_code)
    )
    await BecomeToSeller.wait_category.set()
