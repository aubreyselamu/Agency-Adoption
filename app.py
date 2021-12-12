from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config["SECRET_KEY"] = "Yohanna_12"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route('/')
def homepage():
    '''List all pets in homepage'''
    
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)
