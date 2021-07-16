from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message

from app.data.text.ru.default.button.reply import agree_rules
from app.loader import dp
from app.data import text
from app.states.private.registration_new_user import RegistrationNewUser


@dp.message_handler(state=RegistrationNewUser.agree_rules, reply_command=agree_rules)
async def agree_rules(message: Message, state: FSMContext, user, lang_code):
    await state.finish()
    await message.answer(
        text=text[lang_code].default.message.good
    )
    await user.update_data(is_read_rules=True)
    raise SkipHandler()
