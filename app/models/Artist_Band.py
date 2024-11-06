from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class ArtistBand(db.Model):
    __tablename__ = 'artist_band'

    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.artist_id'), primary_key=True)
    band_id: Mapped[int] = mapped_column(ForeignKey('band.band_id'), primary_key=True)