from sqlalchemy import Column, BigInteger, Sequence, String, Float, Integer

from app.data.types.bargain_data import BargainStatusType, BargainRate, BargainFeedback
from app.utils.db_api.db import BaseModel


class Bargain(BaseModel):
    __tablename__ = 'bargains_trigon'
    id: int = Column(BigInteger, Sequence('bargain_id'), primary_key=True)
    status: str = Column(String(15), default=BargainStatusType.ACTIVE)
    seller_user_id: int = Column(BigInteger)
    buyer_user_id: int = Column(BigInteger)
    amount: float = Column(Float(precision=1, asdecimal=True, decimal_return_scale=True))
    category: str = Column(String(40), default='')
    title: str = Column(String(30), default='')
    commission_amount: int = Column(Integer)
    rate: int = Column(Integer, default=BargainRate.NONE)
    feedback: str = Column(String(150), default=BargainFeedback.NONE)
