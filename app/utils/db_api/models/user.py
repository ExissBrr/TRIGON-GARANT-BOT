import datetime as dt
from typing import List, Union

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime, Integer

from app.data.types.user_data import UserRole, UserDeepLink, UserPhone, UserDataHistory
from app.loader import config
from app.utils.db_api.db import BaseModel


class User(BaseModel):
    __tablename__ = 'users_template'

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

    online_at: dt.datetime = Column(DateTime(), default=dt.datetime.utcnow())

    @property
    def url_to_telegram(self) -> str:
        return f"tg://user?id={self.id}"

    def is_role(self, roles: Union[str, List[str]]) -> bool:
        if isinstance(roles, list):
            return self.role in roles
        return self.role == roles
    @property
    def get_username_history(self) -> list:
        return self.username_history.rstrip().splitlines()
    @property
    def get_fullname_history(self) -> list:
        return self.fullname_history.rstrip().splitlines()

    async def update_fullname(self, fullname):
        if self.fullname == fullname:
            return False
        self.fullname_history += fullname + '\n'
        await self.update_data(fullname_history=self.fullname_history)
        await self.update_data(fullname=fullname)

    async def update_username(self, username):
        if self.username == username:
            return False

        self.username_history += str(self.username) + '\n'
        await self.update_data(username_history=self.username_history)
        await self.update_data(username=username)
