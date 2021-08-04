from sqlalchemy import Column, BigInteger, Sequence, String, ForeignKey

from app.utils.db_api.db import BaseModel


class UserRequisite(BaseModel):
    __tablename__ = 'user_requisites'

    id: int = Column(BigInteger, Sequence('requisite_id'))

    requisite: str = Column(String, primary_key=True)
    status: str = Column(String)
    user_id: int = Column(ForeignKey('users.id'), primary_key=True)
