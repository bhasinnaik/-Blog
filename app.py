from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  version = db.Column(db.String(3))
  title = db.Column(db.String(50))
  subtitle = db.Column(db.String(50))
  author = db.Column(db.String(20))
  date_posted = db.Column(db.DateTime)
  content = db.Column(db.Text)

@app.route('/')
def index():
  return render_template('index.html')