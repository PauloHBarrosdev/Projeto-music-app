from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class UserFavoriteCategory(db.Model):
    __tablename__ = 'user_favorite_category'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'),primary_key=True)
    band_id: Mapped[int] = mapped_column(ForeignKey('category.category_id'), primary_key=True)
