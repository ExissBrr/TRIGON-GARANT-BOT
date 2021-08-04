from sqlalchemy import Column, BigInteger, String, Sequence, Boolean

from app.utils.db_api.db import BaseModel


class Feedback(BaseModel):
    __tablename__ = "Feedback"
    id: int = Column(BigInteger, Sequence("feedback_counter"), primary_key=True)
    seller_user_id: int = Column(BigInteger, default=None)
    rate: int = Column(BigInteger, default=-1)
    buyer_user_id: int = Column(BigInteger, default=None)
    feedback: str = Column(String(200), default="None")
    status_hide: bool = Column(Boolean, default=True)
    status_buyer_hide: bool = Column(Boolean, default=True)

    async def update_status_hide(self, new_status_hide: bool):
        await self.update_data(status_hide=new_status_hide)

    async def update_status_buyer_hide(self, new_status_buyer_hide: bool):
        await self.update_data(status_buyer_hide=new_status_buyer_hide)

    async def update_feedback(self, new_comment: str):
        await self.update_data(feedback=new_comment)

    async def update_rate(self, new_rate: int):
        await self.update_data(rate=new_rate)
