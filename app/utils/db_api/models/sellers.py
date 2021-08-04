from sqlalchemy import Column, BigInteger, String, Sequence, ForeignKey

from app.data.types.seller_data import SellerStatus
from app.utils.db_api.db import BaseModel


class Seller(BaseModel):
    __tablename__ = 'sellers'
    id: int = Column(BigInteger, Sequence('seller_id'), primary_key=True)
    user_id: int = Column(BigInteger)
    status: str = Column(String, default=SellerStatus.APPROVAL)
    description: str = Column(String(400), default='-')
    category_id: int = Column(ForeignKey('service_categories.id'))

    async def update_status(self, new_status):
        await self.update_data(status=new_status)
