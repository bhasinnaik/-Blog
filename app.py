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
# return all blogs with latest one first.
@app.route('/')
def index():
  posts = Blog.query.order_by(Blog.date_posted.desc()).all()
  return render_template('index.html', posts=Blog.query.all( ))

#route to return specific blog details once user clicks on specific blog on index.html.
@app.route('/post/<int:post_id>')
def post(post_id):
  post = Blog.query.filter_by(id=post_id).one()
  return render_template('post.html', post=post)
