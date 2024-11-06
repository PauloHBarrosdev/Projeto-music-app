from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Feat(db.Model):
    __tablename__ = 'feat'
    feat_id: Mapped[int] = mapped_column(primary_key=True)