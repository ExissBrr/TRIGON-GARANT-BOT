from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSending
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(state=MessageSending.confirm_schedule)
async def add_schedule_in_db(message: Message, state: FSMContext, user, lang_code, state_data: dict):
    distribution_message = state_data.get('mess', None)
    distribution_urls: dict = state_data.get('urls', None)
    distribution_media = state_data.get('media_id', None)
    distribution_media_type = state_data.get('media_type', None)
    distribution_time = state_data.get('time', None)
    links = ''
    for title, link in distribution_urls.items():
        links += f"{title}:{link} "
    links = links.strip()
    await MessageForSending.insert(
        content_type=distribution_media_type,
        media_id=distribution_media,
        text=distribution_message,
        links_btn=links,
        time=distribution_time
    )
    await message.answer(
        text=text[lang_code].default.message.added
    )
    await send_main_keyboard(user, state)
