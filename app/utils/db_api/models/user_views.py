from sqlalchemy import Column, BigInteger, Sequence

from app.utils.db_api.db import BaseModel


class UserView(BaseModel):
    __tablename__ = 'user_views'
    id = Column(BigInteger, Sequence('user_view_id'), primary_key=True)
    viewer_user_id = Column(BigInteger)
    user_id = Column(BigInteger)
