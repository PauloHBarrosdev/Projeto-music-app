from app import db
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class Album(db.Model):
    __tablename__ = 'album'

    album_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    duration: Mapped[float]
    feat: Mapped[int] = mapped_column(ForeignKey("feat.feat_id"))