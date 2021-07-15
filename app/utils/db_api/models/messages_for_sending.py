import datetime

from aiogram.types import ContentType
from loguru import logger
from sqlalchemy import Column, BigInteger, Sequence, String, Integer, DateTime, Boolean

from app.utils.db_api.db import BaseModel


class MessageForSending(BaseModel):
    __tablename__ = 'messages_for_sending_template'
    id: int = Column(BigInteger, Sequence('message_for_sending_id'))
    is_active: bool = Column(Boolean, default=True)
    content_type: str = Column(String, default=ContentType.TEXT)
    media_id: str = Column(String)
    text: str = Column(String(200))
    links_btn: str = Column(String)
    time: str = Column(String(30))

    def is_content_type(self, content_type: str) -> bool:
        return self.content_type == content_type

    @property
    def get_links_btn(self) -> dict:
        if self.links_btn is None:
            return {}
        links_btn = {}
        for link_data in self.links_btn.split():
            title = link_data.split(':')[0]
            link = ''.join(link_data.split(':')[1:])
            links_btn.setdefault(title, link)
        logger.debug(links_btn)
        return links_btn
