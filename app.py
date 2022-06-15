from flask import Flask, render_template

app = Flask(__name__)

@app.route('/abc')
def index():
  return render_template('index.html')

@app.route('/abc/signup')
def signup():
  return render_template('signup_modal.html')

@app.route('/signup_modal.html')
def signup_index():
  return render_template('signup_modal.html')



