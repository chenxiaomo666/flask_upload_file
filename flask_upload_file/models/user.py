from .. import db
import datetime


class User(db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(64))
    passwd = db.Column("passwd", db.Text)
    register_time = db.Column("register_time", db.DateTime, default=datetime.datetime.now())
    last_login_time = db.Column("last_login_time", db.DateTime)
    is_delete = db.Column("is_delete", db.Integer, default=0)