from sqlalchemy import Column, BigInteger, Sequence, String

from app.utils.db_api.db import BaseModel


class ServiceCategory(BaseModel):
    __tablename__ = 'service_categories'

    id: int = Column(BigInteger, Sequence("service_category_id"), primary_key=True)

    title: str = Column(String(36))
    description: str = Column(String(200))
    photo_link: str = Column(String(400))
