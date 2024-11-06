from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Music(db.Model):
    __tablename__ = 'music'

    music_id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int] = mapped_column(ForeignKey('category.category_id'))
    main_artist: Mapped[int] = mapped_column(ForeignKey('artist.artist_id'))
    feat: Mapped[int] = mapped_column(ForeignKey('feat.feat_id'))
    album: Mapped[int] = mapped_column(ForeignKey('album.album_id'))