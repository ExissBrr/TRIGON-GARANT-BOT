from sqlalchemy import Column, BigInteger, Sequence, String, LargeBinary

from app.utils.db_api.db import BaseModel


class PhotoCache(BaseModel):
    __tablename__ = 'photos_cache'
    id: int = Column(BigInteger, Sequence('_id'), primary_key=True)
    prefix: str = Column(String(30))
    url: str = Column(String(400))
    binary: bytes = Column(LargeBinary)
