"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  """Connect the database to our Flask App."""
  db.app = app
  db.init_app(app)

  

if __name__ == "__main__":
  from app import app
  connect_db(app)

  db.drop_all()
  db.create_all()

Zuck_image = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dailymail.co.uk%2Fsciencetech%2Farticle-13345129%2Fmark-zuckerberg-fall-facebook-ufc-beard.html&psig=AOvVaw1k318Lp7Qq8fHM9qVyMAmt&ust=1717613047962000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCID7g6_NwoYDFQAAAAAdAAAAABAJ"

class User(db.Model):
  """Blog User"""

  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  first_name = db.Column(db.Text, nullable = False)
  last_name = db.Column(db.Text, nullable = False)
  image_url = db.Column(db.Text, nullable = False, default = Zuck_image) 

  @property
  def full_name(self):
    """Return User Full Name"""

    return f"{self.first_name} {self.last_name}"


  