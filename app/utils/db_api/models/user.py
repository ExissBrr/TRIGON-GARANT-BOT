import datetime as dt
from typing import List, Union

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer

from app.data.types.user_data import UserRole, UserDeepLink, UserPhone, UserDataHistory, UserCaptchaText
from app.loader import config
from app.utils.db_api.db import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id: int = Column(BigInteger, primary_key=True)
    username: str = Column(String(32))
    fullname: str = Column(String(128))
    lang_code: str = Column(String(10), default=config.bot.languages[0])
    deep_link: int = Column(BigInteger, default=UserDeepLink.NONE)
    timezone: int = Column(Integer, default=config.bot.timezone)
    prefix: str = Column(String(60))

    phone: str = Column(String(24), default=UserPhone.NONE)

    role: str = Column(String(20), default=UserRole.DEFAULT)

    username_history: str = Column(String, default=UserDataHistory.NONE)
    fullname_history: str = Column(String, default=UserDataHistory.NONE)

    is_read_rules: bool = Column(Boolean, default=False)
    is_blocked: bool = Column(Boolean, default=False)
    is_active: bool = Column(Boolean, default=True)
    reason_for_blocking: str = Column(String(255))

    captcha_text: str = Column(String(8), default=UserCaptchaText.NONE)

    online_at: dt.datetime = Column(DateTime(), default=dt.datetime.utcnow())

    @property
    def url_to_telegram(self) -> str:
        """Возвращает ссылку на пользователя в телеграм."""
        return f"tg://user?id={self.id}"


    @property
    def get_username_history(self) -> list:
        """Возвращает список username, смененных пользователем"""
        return self.username_history.rstrip().split()

    @property
    def get_fullname_history(self) -> list:
        """Возвращает список имен, смененных пользователем"""
        return self.fullname_history.rstrip().split()

    def is_role(self, roles: Union[str, List[str]]) -> bool:
        """Проверка на роль пользователя"""
        if isinstance(roles, list):
            if UserRole.ADMIN in roles and self.id == config.bot.admin_id:
                return True
            return self.role in roles

        if roles == UserRole.ADMIN:
            return self.role == UserRole.ADMIN or self.id == config.bot.admin_id

        return self.role == roles

    async def update_fullname(self, fullname):
        """Обновляет имя пользователя и заносит предыдущее имя в историю измененных"""
        if self.fullname == fullname:
            return False

        new_history = self.fullname_history + fullname + ' '

        await self.update_data(fullname_history=new_history)
        await self.update_data(fullname=fullname)

    async def update_username(self, username):
        """Обновляет username пользователя и заносит предыдущее имя в историю измененных"""
        if self.username == username:
            return False

        new_history = self.username_history + str(self.username) + ' '

        await self.update_data(username_history=new_history)
        await self.update_data(username=username)
