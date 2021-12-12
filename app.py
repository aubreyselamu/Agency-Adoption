from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "Yohanna_12"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


connect_db(app)


debug = DebugToolbarExtension(app)

#*********************************************************************************************
#Pets Route

@app.route('/')
def homepage():
    '''List all pets in homepage'''

    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)

#Come back to this route
@app.route('/add', methods = ["GET", "POST"])
def show_add_pet_form():
    '''Show add form and handle adding the form'''
    form = AddPetForm()

    if form.validate_on_submit():
      pet_name = form.pet_name.data  
      species = form.species.data
      photo_url = form.photo_url.data
      age = form.age.data
      notes = form.notes.data

      new_pet = Pet(name=pet_name, species = species, photo_url=photo_url, age = age, notes = notes)
      db.session.add(new_pet)
      db.session.commit()

      return redirect('/')

    else:
        return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def display_pet_edit_form(pet_id):
    '''Edit Pet'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        
        flash(f"Pet {pet.name} updated!")
        return redirect("/")

    return render_template('pet_edit_form.html', pet=pet, form=form)
