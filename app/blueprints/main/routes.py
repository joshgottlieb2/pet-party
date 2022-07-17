from flask import render_template, url_for, redirect, request, flash
from app import db
from app.blueprints.auth.forms import PetForm
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

@app.route("/adopt/<int:id>", methods=['GET', 'POST'])
def adopt(id):
    owner = None
    form=PetForm()
    pet_to_update = Pet.query.get(id)
    if request.method == "POST":
        pet_to_update.owner = request.form['owner']
        try:
            db.session.commit()
            flash("You have successfully adopted your new pet!")
            return redirect("/")
        except:
            flash("Error.  Try again.")
            return render_template("/adopt.html", form=form, pet_to_update=pet_to_update)

    else:
        return render_template("/adopt.html", form=form, pet_to_update=pet_to_update)

    # if form.validate_on_submit():
    #     owner = form.owner.data
    #     form.owner.data = ''
    return render_template('adopt.html/<int:id>', owner=owner, form=form)

