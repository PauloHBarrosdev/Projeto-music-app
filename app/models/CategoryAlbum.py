from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class CategoryAlbum(db.Model):
    __tablename__ = 'category_album'

    category_id: Mapped[int] = mapped_column(ForeignKey('category.category_id'), primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey('album.album_id'), primary_key=True)