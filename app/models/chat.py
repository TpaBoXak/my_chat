from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy import ForeignKey

from datetime import datetime

from .base import Base

class UserChat(Base):
    __tablename__ = "users_chats"
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey('chats.id'), 
            nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'),
            nullable=False)

class Chat(Base):
    __tablename__ = "chats"
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    is_group: Mapped[bool] = mapped_column(Boolean, nullable=False)
    time_created: Mapped[datetime] = mapped_column(DateTime, nullable=False,
            server_default=func.now())
