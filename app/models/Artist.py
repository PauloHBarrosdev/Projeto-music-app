from app import db
from sqlalchemy import ForeignKey, Date, String
from sqlalchemy.orm import Mapped, mapped_column

class Artist(db.Model):
    __tablename__ = 'artist'
    
    artist_id: Mapped[int] = mapped_column(primary_key=True)
    main_category: Mapped[int] = mapped_column(ForeignKey('category.category_id'))
    name: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[Date] = mapped_column(Date)