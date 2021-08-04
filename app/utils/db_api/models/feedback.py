from sqlalchemy import Column, BigInteger, String, Sequence

from app.data.types.feedback_data import FeedbackStatus
from app.utils.db_api.db import BaseModel


class Feedback(BaseModel):
    __tablename__ = "feedbacks"
    id: int = Column(BigInteger, Sequence("feedback_id"), primary_key=True)
    status: str = Column(String, default=FeedbackStatus.ACTIVE)
    receiver_user_id: int = Column(BigInteger)
    rate: int = Column(BigInteger, default=-1)
    commentator_user_id: int = Column(BigInteger)
    comment: str = Column(String(200), default="None")
