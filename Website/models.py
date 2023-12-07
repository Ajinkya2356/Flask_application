from . import db
import datetime


class Users(db.Model):
    __tablename__ = "user"
    is_active = True
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    username=db.Column(db.String(30),nullable=False)