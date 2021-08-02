from typing import List

from aiogram.types import ContentType
from sqlalchemy import Column, BigInteger, Sequence, String, Boolean

from app.data.types.user_data import UserRole
from app.utils.db_api.db import BaseModel


class MessageForSending(BaseModel):
    __tablename__ = 'messages_for_sending'
    id: int = Column(BigInteger, Sequence('message_for_sending_id'), primary_key=True)
    is_active: bool = Column(Boolean, default=True)
    content_type: str = Column(String, default=ContentType.TEXT)
    media_id: str = Column(String)
    text: str = Column(String(200))
    links_btn: str = Column(String)
    time: str = Column(String(30))
    chats_id: str = Column(String(100))
    roles: str = Column(String(50))

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
        return links_btn

    @property
    def get_chats_id(self) -> List[int]:
        if not self.chats_id:
            return []
        return [int(chat_id) for chat_id in self.chats_id.split()]

    @property
    def get_roles(self) -> List[str]:
        if not self.chats_id:
            return []
        return [role for role in self.roles.split() if role in UserRole.__dict__.values()]
