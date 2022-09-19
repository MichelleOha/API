from flask import Blueprint
from main import db
from models.person import Person

person = Blueprint('person', __name__, url_prefix="/person")

@person.route("/", methods=["GET"])
def get_person():
    #get all the person from db
    person_list = Person.query.all()
    
    return "Person list"