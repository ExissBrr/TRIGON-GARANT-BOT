from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.wait_for_url)
async def wait_for_media(message: Message, state: FSMContext, lang_code):
    raw_data = message.text.split()
    links = ''
    for data in raw_data:
        try:
            title, link = data.split(':')
            if 'http' in link:
                links += f"{title}:{link} "
        except Exception:
            pass
    links = links.strip()
    await state.update_data(urls=links)
    await message.answer(
        text=text[lang_code].admin.message.send_media
    )
    await MessageSending.wait_for_media.set()
