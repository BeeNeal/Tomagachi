"""Models and database functions for Tomagachi project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """User of Tomagachi website."""

    __tablename__ = "users"

    user_id = db.column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """provide representation when printed"""

        return "User user_id={} email={}>" .format(self.user_id, self.email)

# Question: For storing my class objects in DB, need to store object only,
# perhaps with unique ID, or need to separate out each attribute value?


class Tomagachi(db.Model):
    """Gachis belonging to user"""

    __tablename__ = "tomagachis"

    gachi_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
