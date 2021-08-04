from sqlalchemy import Column, BigInteger, Sequence

from app.utils.db_api.db import BaseModel


class View(BaseModel):
    __tablename__ = 'Views'
    id = Column(BigInteger, Sequence('id_views'), primary_key=True)
    viewer_user_id = Column(BigInteger)
    user_id = Column(BigInteger)
