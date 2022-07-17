from flask import render_template, url_for, redirect
from . import bp as app
from app.blueprints.main.models import Pet
from flask_login import login_required, current_user


@app.route("/")
def home():

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    pets = Pet.query.all()
    context = {
        "pets": pets,
        "user": current_user
    }
    return render_template('index.html', **context)

@app.route("/my_pets")
def my_pets():
    pets = Pet.query.all()
    context = {
        "pets": pets,
        "user": current_user
    }
    return render_template('my_pets.html', **context)


