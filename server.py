"""Tomagachi server"""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request,
                   flash, session)
from flask_debugtoolbar import DebugToolbarExtension

# from toma_class import *

from model import connect_to_db, db, User, Tomagachi

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


# gachis = [HappyTomagachi('Zeus'), HappyTomagachi('my first toma!'), HappyTomagachi('doc')]
joy = User(first_name='Joy', last_name='Neal', email='jgwenn@gmail.com',
           password='abc123')


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/registration')
def display_registration_form():
    """displays registration form"""

    return render_template("registration_form.html")


@app.route('/registration', methods=['POST'])
def registration():
    """Stores user info to DB"""

    email = request.form.get("login_email")
    password = request.form.get("login_password")
    password_match = request.form.get("login_password2")
    f_name = request.form.get("first_name")
    l_name = request.form.get("last_name")

    email_status = User.query.filter(User.email == email).first()

    if email_status is None and password == password_match:
        new_user = User(email=email, password=password,
                        first_name=f_name, last_name=l_name)
        db.session.add(new_user)
        db.session.commit()

    flash("Registration for User {} successful") .format(email)
# WIP
# @app.route('/login', methods=['POST'])
# def login():
#     """stores email/password to DB"""

#     email = request.form.get("login_email")
#     password = request.form.get("login_password")
    #how to store these to DB? -> create user instance
    #if email in DB, add to session to login
    # if not in DB, add to DB, add to session to login

#task, query a user's email
    # if email == User.query.get(email):


    # else:
    #     new_user = User(email=email, password=password)
    #     db.session.add(auden)
    #     db.session.commit()

# @app.route('/login')
# def login():
#     """display login page"""

#     return render_template('login.html')


@app.route('/gachi/create', methods=['GET'])
def create_page():
    """renders creation page"""

    return render_template("create.html")


@app.route('/gachi/create', methods=['POST'])
def create_post():
    """creates instance of gachi from user input"""

    gachi_name = request.form.get("gachi_name")

    gachi_instance = HappyTomagachi(gachi_name)
    gachis.append(gachi_instance)

    return redirect("/view_gachis")


@app.route('/view_gachis')
def gachi_list():
    """lists all gachis that have ever been created"""

    return render_template("gachis.html", gachis=gachis)


@app.route('/gachi/<gachi_name>')
# The variable is passed from the URL into the function
def indiv_gachi(gachi_name):
    """individual gachi profile with feeding option"""

    for item in gachis:
        if item.name == gachi_name:
            gachi = item

    return render_template("gachi.html", gachi=gachi)


@app.route('/gachi/<gachi_name>/feed', methods=['POST'])
def feed(gachi_name):
    """decreases gachi hunger"""

    feed = request.form.get("option")

    for item in gachis:
        if item.name == gachi_name:
            gachi = item

    food_type = request.form.get("food_type")

    gachi.eat(food_type)

    return redirect("/gachi/{}".format(gachi_name))


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True


    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

# Q: tamagochi show page vs tamagachi index <- list
