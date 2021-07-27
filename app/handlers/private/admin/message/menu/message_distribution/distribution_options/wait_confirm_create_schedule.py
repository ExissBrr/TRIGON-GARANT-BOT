from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType
from loguru import logger

from app import keyboards
from app.data import text
from app.data.text.ru.button.reply import confirm
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(state=MessageSendingStates.wait_confirm_create_schedule, text=confirm)
async def add_schedule_in_db(message: Message, state: FSMContext, user, lang_code, state_data: dict):
    await send_main_keyboard(user, state)
    distribution_message = state_data.get('mess', None)
    distribution_urls: dict = state_data.get('urls', {})
    distribution_media = state_data.get('media_id', None)
    distribution_media_type = state_data.get('media_type', ContentType.TEXT)
    distribution_time = state_data.get('time', '15:00')
    distribution_chats_id = state_data.get('main_chats_id', None)
    links = ''
    for title, link in distribution_urls.items():
        links += f"{title}:{link} "
    links = links.strip()
    await MessageForSending.insert(
        content_type=distribution_media_type,
        media_id=distribution_media,
        text=distribution_message,
        links_btn=links,
        time=distribution_time,
        chats_id=distribution_chats_id,
    )
    await message.answer(
        text=text[lang_code].default.message.added
    )
