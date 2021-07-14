from sqlalchemy import Column, BigInteger, Sequence, String

from app.utils.db_api.db import BaseModel


class StartLinkHistory(BaseModel):
    __tablename__ = 'start_link_history'

    id: int = Column(BigInteger, Sequence('start_link_id'), primary_key=True)
    type: str = Column(String(12))
    prefix: str = Column(String(64))
    args: str = Column(String(64))
    user_id: str = Column(BigInteger)
