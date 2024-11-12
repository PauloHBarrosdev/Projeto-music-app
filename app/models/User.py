from app import db, ma
from marshmallow import fields
from sqlalchemy import ForeignKey, Date, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    __tablename__ = 'user'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =  mapped_column(String(40))
    user_group: Mapped[int] = mapped_column(ForeignKey("user_group.user_group_id"))
    birth_date: Mapped[Date] = mapped_column(Date)
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(300))

class UserSchema(ma.Schema):
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    user_group = fields.Int(required=True)
    birth_date = fields.Date(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)