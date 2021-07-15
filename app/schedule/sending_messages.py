import datetime
from typing import List

from loguru import logger

from app.keyboards.default.inline import generator_button_url
from app.utils.bot import sending_message
from app.utils.db_api.models.messages_for_sending import MessageForSending


async def sending_notifications():
    time_now = datetime.datetime.utcnow()
    time_h_m = f'{time_now.hour}:{time_now.minute}'
    logger.debug(time_h_m)
    messages: List[MessageForSending] = await MessageForSending.query.where(
        MessageForSending.qf(
            time=time_h_m
        )
    ).gino.all()

    for message in messages:
        await sending_message.text_message(
            content_type=message.content_type,
            file_id=message.media_id,
            text=message.text,
            markup=generator_button_url.keyboard(message.get_links_btn),
        )

