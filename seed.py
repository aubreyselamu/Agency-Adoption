from models import Pet, db
from app import app

db.drop_all()
db.create_all()

#If User table isn't empty, empty it
Pet.query.delete()

#Add Pets
nipsey = Pet(name = "Nipsey", species = "Doberman", age=1,)
roman = Pet(name = "Roman", species = "German Shepherd", age=1,)
king = Pet(name = "King", species = "Pitbull", age =2 )

#Add new objects to session
db.session.add(nipsey)
db.session.add(roman)
db.session.add(king)

#Commit to session
db.session.commit()