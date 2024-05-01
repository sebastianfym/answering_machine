import datetime
import enum
from sqlalchemy import Enum, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db.config import Base


class Status(enum.Enum):
    alive = "alive"
    dead = "dead"
    finished = "finished"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(Enum(Status), default=None)
    status_updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    def __repr__(self):
        return f"User(id={self.id}, chat_id={self.chat_id}, " \
               f"created_at={self.created_at}, status={self.status}, " \
               f"status_updated_at={self.status_updated_at})"

