from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class BandFeat(db.Model):
    __tablename__ = 'band_feat'

    band_id: Mapped[int] = mapped_column(ForeignKey('band.band_id'), primary_key=True)
    feat_id: Mapped[int] = mapped_column(ForeignKey('feat.feat_id'), primary_key=True)