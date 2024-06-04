"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_bloggly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SeahawksRule"

connect_db(app)

toolbar = DebugToolbarExtension(app)
app.debug = True


@app.route('/')
def root():
  """Homepage redirects to list of users"""

  return redirect("/users")


@app.route('/users')
def users_list():
  """Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form."""

  users = User.query.order_by(User.last_name, User.first_name).all()
  return render_template('users/index.html', users = users)


@app.route('/users/new', methods = ["GET"])
def new_users_form():
  """Show form to create new user"""

  return render_template('users/new.html')

@app.route("/users/new", methods = ["POST"])
def new_users():
  """Takes form submission, creates new user"""

  new_user = User (first_name = request.form['first_name'], 
                   last_name = request.form ['last_name'],
                   image_url = request.form ['image_url'] or None)
  
  db.session.add(new_user)
  db.session.commit()

  return redirect ("/users")


@app.route('/users/<int: user_id>')
def show_users(user_id):
  """Show information on given user. Have button to get to their edit page, and to delete the user"""

  user = User.query.get_or_404(user_id)
  return render_template('users/show.html', user = user)


@app.route('/users/<int: user_id>/edit')
def edit_users(user_id):
  """Show edit page for user. Have cancel button that returns to detail page for user, and save button that updates user"""

  user = User.query.get_or_404(user_id)
  return render_template('users/show.html', user = user)

@app.route('/users/<int: user_id>/edit', methods = ["POST"])
def update_users(user_id):
  """Process the edit form, returning the user to the /users page"""

  user = User.query.get_or_404(user_id)
  user.first_name = request.form ['first_name']
  user.last_name = request.form ['last_name']
  user.image_name = request.form ['image_url']

  db.session.add(user)
  db.session.commit()

  return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods = ["POST"])
def delete_user(user_id):
  """Handle form submission to delete the user"""

  user = User.query.get_or_404(user_id)
  db.session.delete(user)
  db.session.commit()
  
  return redirect ("/users")










