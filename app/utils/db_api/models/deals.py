from sqlalchemy import Column, BigInteger, Sequence, String, Float, Integer, ForeignKey

from app.data.types.bargain_data import DealStatusType, FeedbackRate, DealFeedback
from app.utils.db_api.db import BaseModel


class Deal(BaseModel):
    __tablename__ = 'deals'
    id: int = Column(BigInteger, Sequence('deal_id', start=8000), primary_key=True)
    status: str = Column(String(15), default=DealStatusType.ACTIVE)
    seller_user_id: int = Column(ForeignKey('users.id'))
    buyer_user_id: int = Column(ForeignKey('users.id'))
    amount: float = Column(Float(precision=1, asdecimal=True, decimal_return_scale=True))
    category_id: str = Column(ForeignKey('service_categories.id'))
    title: str = Column(String(30), default='')
    feedback_id: str = Column(ForeignKey('feedbacks.id'))
