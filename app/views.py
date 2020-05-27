from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/store')
def store():
    return render_template('store.html', title='Дэлгүүр')


@app.route('/cart')
def cart():
    return render_template('cart.html', title='Сагс')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Нэвтрэх', form=form)
