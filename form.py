from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField

class AddPetForm(FlaskForm):
    '''Form for adding pets'''

    pet_name = StringField("Pet Name")
    species = SelectField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
