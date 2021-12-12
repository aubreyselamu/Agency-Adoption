from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm

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

@app.route('/add', methods = ["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
      pet_name = form.pet_name.data  
      species = form.species.data
      photo_url = form.photo_url.data
      age = form.age.data
      notes = form.notes.data

      return redirect('/')

    else:
        return render_template('add_pet.html', form=form)