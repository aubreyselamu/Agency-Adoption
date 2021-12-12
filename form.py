from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import Length, NumberRange, URL, Optional, InputRequired

class AddPetForm(FlaskForm):
    '''Form for adding pets'''

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'),('dog', 'Dog'),('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators = [URL(), Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0,max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators = [URL(), Optional()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")