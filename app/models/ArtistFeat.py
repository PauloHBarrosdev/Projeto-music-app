from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class ArtistFeat(db.Model):
    __tablename__ = 'artist_feat'

    artist_id: Mapped[int] = mapped_column(ForeignKey('artist.artist_id'), primary_key=True)
    feat_id: Mapped[int] = mapped_column(ForeignKey('feat.feat_id'), primary_key=True)