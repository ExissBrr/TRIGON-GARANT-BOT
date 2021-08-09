from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.payment_data import PaymentSystemStatus, PaymentType
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.utils.db_api.models.payment_systems import PaymentSystem
from app.utils.db_api.models.user import User


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.top_up_balance))
async def send_menu_choice_payment_system(call: CallbackQuery, user: User, lang_code):
    payment_systems = await PaymentSystem.query.distinct(PaymentSystem.system).where(
        PaymentSystem.status == PaymentSystemStatus.ACTIVE).gino.all()
    if not payment_systems:
        return await call.answer(
            text=text[lang_code].default.call.balance_top_up_is_unavailable
        )
    else:
        await call.answer(
            cache_time=5,
            text='One moment..'
        )
    await call.message.answer(
        disable_web_page_preview=True,
        text=text[lang_code].default.message.choice_payment_system,
        reply_markup=keyboards.default.inline.balance.payment_system_list.keyboard(PaymentType.IN, payment_systems,
                                                                                   lang_code)
    )
