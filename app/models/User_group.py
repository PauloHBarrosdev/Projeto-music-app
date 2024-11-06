from app import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User_group(db.Model):
    __tablename__ = 'user_group'

    user_group_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    permitions: Mapped[str] = mapped_column(String(4))