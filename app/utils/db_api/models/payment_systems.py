from sqlalchemy import Column, BigInteger, Sequence, String

from app.data.types.payment_data import PaymentSystemStatus
from app.utils.db_api.db import BaseModel


class PaymentSystem(BaseModel):
    __tablename__ = 'payment_systems'

    id: int = Column(BigInteger, Sequence('payment_system_id'), primary_key=True)
    title: str = Column(String)
    system: str = Column(String)
    token: str = Column(String)
    account_wallet: str = Column(String)
    status: str = Column(String, default=PaymentSystemStatus.INACTIVE)
