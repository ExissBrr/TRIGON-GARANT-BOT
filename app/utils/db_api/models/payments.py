from sqlalchemy import Column, BigInteger, Sequence, String, Float, ForeignKey

from app.data.types.payment_data import PaymentStatus, PaymentTransactionId
from app.utils.db_api.db import BaseModel


class Payment(BaseModel):
    __tablename__ = 'payments'
    id: str = Column(BigInteger, Sequence('payment_id'), primary_key=True)
    transaction_id: str = Column(String(100), default=PaymentTransactionId.NONE)
    comment: str = Column(String(36), Sequence('payment_comment', start=6416, increment=7))
    type: str = Column(String(20))
    status: str = Column(String(20), default=PaymentStatus.PENDING)
    commission_amount: float = Column(Float(precision=1, asdecimal=True, decimal_return_scale=True))
    amount: float = Column(Float(precision=1, asdecimal=True, decimal_return_scale=True))
    payer_user_id: int = Column(ForeignKey('users.id'))
    system_id: int = Column(ForeignKey('payment_systems.id'))
    account_from: str = Column(String(30))
    account_in: str = Column(String(30))
