from sqlalchemy import Column, BigInteger, String, Sequence

from app.utils.db_api.db import BaseModel


class SellerStatus:
    HIDDEN: int = 'hidden'
    APPROVAL: int = 'approval'
    ACTIVE: int = 'active'


class Seller(BaseModel):
    __tablename__ = 'Sellers'
    id: int = Column(BigInteger, Sequence('id_seller'), primary_key=True)
    user_id: int = Column(BigInteger)
    status: str = Column(String, default=SellerStatus.APPROVAL)
    description: str = Column(String(400), default='-')
    category: str = Column(String(200))

    async def update_status(self, new_status):
        await self.update_data(status=new_status)
