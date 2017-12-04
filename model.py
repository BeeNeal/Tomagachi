"""Models and database functions for Tomagachi project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """User of Tomagachi website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    owned = db.relationship('Tomagachi', backref=db.backref('owned', lazy=True))

    def __repr__(self):
        """provide representation when printed"""

        return "<User user_id={} email={}>" .format(self.user_id, self.email)


class Tomagachi(db.Model):
    """Gachis belonging to user"""

    __tablename__ = "tomagachis"

    gachi_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=30)
    motto = db.Column(db.String(64), nullable=True, default=
                      "Every day is the best day!")
    favorite_food = db.Column(db.String(64), nullable=True, default='pickles')
    owner = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):

        return "<Gachi gachi_id= {} \n name={}>" .format(self.gachi_id, self.name)

    def eat(self, food="grub"):
        """feeds toma - hunger decreases based on type/amount of food"""

        if food == "grub":
            self.hunger -= 1
        elif food == "pistachios":
            self.hunger -= 2
        elif food == "vindaloo":
            self.hunger -= 5
        elif food == self.favorite_food:
            self.hunger = 0
        else:
            self.hunger += 1
        return self.hunger


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tomagachis'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
