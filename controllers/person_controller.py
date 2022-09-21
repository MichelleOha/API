from flask import Blueprint, request
from main import db
from models.person import Person
from schemas.person_schema import person_schema, persons_schema

person = Blueprint('person', __name__, url_prefix="/person")

@person.route("/", methods=["GET"])
def get_persons():
    #get all the person from db
    persons_list = Person.query.all()
    result = persons_schema.dump(persons_list)
    return(result)

@person.route("/<int:id>", methods=["GET"])
def get_person(id):
    #get an item from db by id
    person = Person.query.get(id)
    if not person:
        return {"SORRY": "This person id doesn't exist."}
    result = person_schema.dump(person)
    return(result) 

@person.route("/", methods=["POST"])
def create_person():
    person_fields = person_schema.load(request.json)
    person = Person(
        name = person_fields["name"],
        clothing_size = person_fields["clothing_size"],
        shoe_size = person_fields["shoe_size"],
    )
    
    db.session.add(person)
    db.session.commit()
    return(person_schema.dump(person))

@person.route("/<int:id>", methods=["PUT"])
def update_person(id):
    person = Person.query.get(id)
    if not person:
        return {"SORRY":"This person doesn't exist."}
    person_fields = person_schema.load(request.json)
    
    person.name = person_fields["name"]
    person.clothing_size = person_fields["clothing_size"]
    person.shoe_size = person_fields["shoe_size"]
    
    db.session.commit()
    
    return(person_schema.dump(person))
