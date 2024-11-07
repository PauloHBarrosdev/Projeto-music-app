from app import db
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class MusicUserRating(db.Model):
    __tablename__ = 'music_user_listen'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'), primary_key=True)
    music_id: Mapped[int] = mapped_column(ForeignKey('music.music_id'), primary_key=True)
    rate: Mapped[int]
    date: Mapped[Date] = mapped_column(Date)