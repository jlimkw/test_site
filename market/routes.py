from market import app
from market.models import Item
from market.forms import RegisterForm

from flask import Blueprint, render_template, flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    flash("TEST ERROR")
    return render_template('register.html', form=form)