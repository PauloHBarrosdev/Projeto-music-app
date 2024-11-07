from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class MusicUserListen(db.Model):
    __tablename__ = 'music_user_listen'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'),primary_key=True)
    music_id: Mapped[int] = mapped_column(ForeignKey('music.music_id'), primary_key=True)
    qtd_listen: Mapped[int]
    avg_time_list: Mapped[float]


