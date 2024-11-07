from app import db
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

class RelatedCategory(db.Model):
    __tablename__ = 'related_category'

    category_id: Mapped[int] = mapped_column(ForeignKey('category.category_id'), primary_key=True)
    related_category: Mapped[int] = mapped_column(ForeignKey('category.category_id'), primary_key=True)
    
