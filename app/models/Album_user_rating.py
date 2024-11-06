from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Album_user_rating(db.Model):
    __tablename__ = 'album_user_rating'

    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.album_id"), primary_key=True)
    rate: Mapped[int]
    date: Mapped[str]