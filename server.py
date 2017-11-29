"""Tomagachi server"""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request,
                   flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from toma_class import *

# from model import connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently. This fixes
# that, so instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


gachis = [HappyTomagachi('Zeus'), HappyTomagachi('my first toma!'), HappyTomagachi('doc')]


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


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
