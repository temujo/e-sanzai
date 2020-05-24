from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/store')
def store():
    return render_template('store.html')
