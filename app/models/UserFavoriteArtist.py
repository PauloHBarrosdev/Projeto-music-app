from app import db
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class UserFavoriteArtist(db.Model):
    __tablename__ = 'user_favorite_artist'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'),primary_key=True)
    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.artist_id', primary_key=True))