from app import db
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class Band(db.Model):
    __tablename__ = 'band'

    band_id: Mapped[int] = mapped_column(primary_key=True) 
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] =  mapped_column(String(400))
    main_category: Mapped[int] = mapped_column(ForeignKey('category.category_id'))