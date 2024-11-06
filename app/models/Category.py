from app import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Category(db.Model):
    __tablename__= 'category'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))