from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
# Define database URL String
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# DB Object
db = SQLAlchemy(app)

# DB Model
# To create db, import object in python shell and than execute create comment with db object.
class Blog(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  version = db.Column(db.String(3))
  title = db.Column(db.String(50))
  subtitle = db.Column(db.String(50))
  author = db.Column(db.String(20))
  date_posted = db.Column(db.DateTime)
  content = db.Column(db.Text)

#Root Index path.
@app.route('/')
def index():
  posts = Blog.query.all()
  return render_template('index.html', posts=Blog.query.all( ))