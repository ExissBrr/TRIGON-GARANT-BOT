from sqlalchemy import Column, BigInteger, Sequence, String

from app.utils.db_api.db import BaseModel


class ControversyStatusType:
    ACTIVE: str = 'active'
    CLOSED: str = 'closed'


class Controversy(BaseModel):
    __tablename__ = 'Controversy'
    id: int = Column(BigInteger, Sequence('controversy_counter'), primary_key=True)
    status: str = Column(String, default=ControversyStatusType.ACTIVE)
    bargin_id: int = Column(BigInteger)
    caller_id: int = Column(BigInteger)
    expectant_id: int = Column(BigInteger)
    caller_argument: str = Column(String(200), default='-')
    expectant_argument: str = Column(String(200), default='-')

    def is_status(self, status):
        return self.status == status

    async def update_status(self, new_status):
        await self.update_data(status=new_status)

    async def update_argument(self, user_id: int, comment: str):
        if user_id == self.caller_id:
            await self.update_data(caller_argument=comment)
        elif user_id == self.expectant_id:
            await self.update_data(expectant_argument=comment)
