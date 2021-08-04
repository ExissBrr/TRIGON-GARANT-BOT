from sqlalchemy import Column, BigInteger, Sequence, String, Float

from app.data.types.bargain_data import BargainStatusType
from app.utils.db_api.db import BaseModel


class Bargain(BaseModel):
    __tablename__ = "Bargains"
    id: int = Column(BigInteger, Sequence("id_counter", start=8000, increment=1), primary_key=True)
    status: str = Column(String, default=BargainStatusType.ACTIVE)
    amount: float = Column(Float, default=0)
    seller_id: int = Column(BigInteger)
    buyer_id: int = Column(BigInteger)

    def is_status(self, status):
        return self.status == status

    async def update_status(self, new_status):
        await self.update_data(status=new_status)
