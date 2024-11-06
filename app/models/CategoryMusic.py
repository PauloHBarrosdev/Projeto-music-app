from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class CategoryMusic(db.Model):
    __tablename__ = 'category_music'

    category_id: Mapped[int] = mapped_column(ForeignKey('category.category_id'), primary_key=True)
    music_id: Mapped[int] = mapped_column(ForeignKey('music.music_id'), primary_key=True)