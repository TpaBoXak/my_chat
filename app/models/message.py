from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import func

from datetime import datetime

from .base import Base

class Message(Base):
    __tablename__ = "message"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"),
            nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.id"),
            nullable=False)
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, nullable=False,
            server_default=func.now())