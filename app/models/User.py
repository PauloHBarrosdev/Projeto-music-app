from app import db
from sqlalchemy import ForeignKey, Date, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    __tablename__ = 'user'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =  mapped_column(String(40))
    user_group: Mapped[int] = mapped_column(ForeignKey("user_group.user_group_id"))
    birth_date: Mapped[Date] = mapped_column(Date)
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(300))