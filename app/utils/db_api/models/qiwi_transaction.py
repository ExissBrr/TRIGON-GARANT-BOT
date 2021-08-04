from sqlalchemy import Column, String, Float, BigInteger, Boolean

from app.utils.db_api.db import BaseModel


class QiwiTransactionType:
    TYPE: str = "type"
    IN = 'IN'
    OUT = 'OUT'


class QiwiTransaction(BaseModel):
    __tablename__ = 'QiwiTransactions'
    comment: str = Column(String(32), primary_key=True)
    type: str = Column(String(3))
    amount: float = Column(Float, default=0)
    user_id: int = Column(BigInteger)
    user_wallet_account = Column(String)
    commission: int = Column(Float, default=0)
    is_hold: bool = Column(Boolean, default=False)
