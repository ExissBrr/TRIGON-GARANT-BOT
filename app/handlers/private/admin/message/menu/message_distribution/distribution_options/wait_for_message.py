from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.wait_for_delayed_message, content_types=ContentTypes.ANY)
async def wait_for_url(message: Message, state: FSMContext,lang_code):
    if not message:
        await message.answer(
            text='Неккоректные данные'
        )
    await state.update_data(mess=message.text)
    await message.answer(
        text=text[lang_code].admin.message.send_btn_link,
        reply_markup=keyboards.default.reply.skip.keyboard(lang_code)
    )
    await MessageSending.wait_for_url.set()
