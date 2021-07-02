"""Server for travel planner app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User
import crud
import requests, json, os

from jinja2 import StrictUndefined

app = Flask(__name__) # this is the instance of the flask application
app.secret_key = "secret_key"

app.jinja_env.undefined = StrictUndefined

# Routes and view functions

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/destinations')
def show_destinations():
    """Show list of destinations."""

    destinations = crud.get_destinations()

    return render_template('all_destinations.html', destinations=destinations)


@app.route('/destinations/<destination_id>')
def show_destination(destination_id):
    """Show details on a particular destination."""

    destination = crud.get_destination_by_id(destination_id)

    return render_template('destination_details.html', destination=destination)


@app.route('/user', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    user = crud.get_user_by_email(email)
    if user:
        flash('Unable to create an account with that email. Try again.')
    else:
        crud.create_user(email, password, first_name, last_name)
        flash('Account created! Please log in.')

    return redirect('/')


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.first_name}!")

    return redirect("/")


# @app.route('/user/<user_id>')
# def show_user(user_id):
#     """Show details on a particular user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('user_profile.html', user=user)


@app.route('/search')
def search_destination_form():

    return render_template('search_form.html')


@app.route('/search_destination')
def search_destination():

    destination_search = request.args.get("destination")
    result = crud.get_destination_by_name(destination_search)

    return render_template('search_results.html', result=result)


# @app.route('/dropdown_search')
# def search_destination_form():

#     return render_template('search_dropdown.html')


# @app.route('/search_destination_by_dropdown')
# def search_destination_by_dropdown():

#     destination_search = request.args.get("destination")
#     result = crud.get_destination_by_name(destination_search)

#     return render_template('search_dropdown_results.html', result=result)    

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)