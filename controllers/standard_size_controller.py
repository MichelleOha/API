from flask import Blueprint, request
from main import db
from models.standard_size import Standard_Size
from schemas.standard_size_schema import standard_size_schema, standard_sizes_schema
from marshmallow.exceptions import ValidationError

standard_size = Blueprint('standard_size', __name__, url_prefix="/standard_size")

@standard_size.route("/", methods=["GET"])
def get_standard_sizes():
    #get all the person from db
    standard_sizes_list = Standard_Size.query.all()
    result = standard_sizes_schema.dump(standard_sizes_list)
    return(result), 200

@standard_size.route("/<int:id>", methods=["GET"])
def get_standard_size(id):
    #get an item from db by id
    standard_size = Standard_Size.query.get(id)
    if not standard_size:
        return {"SORRY": "This size id doesn't exist."}, 404
    result = standard_size_schema.dump(standard_size)
    return(result), 200

@standard_size.route("/", methods=["POST"])
def create_standard_size():
    standard_size_fields = standard_size_schema.load(request.json)
    standard_size = Standard_Size (
        name = standard_size_fields["name"],
        clothing_size = standard_size_fields["clothing_size"],
        shoe_size = standard_size_fields["shoe_size"],
        users_id = standard_size_fields["users_id"]
    )
    
    db.session.add(standard_size)
    db.session.commit()
    return(standard_size_schema.dump(standard_size)), 201

@standard_size.route("/<int:id>", methods=["DELETE"])
def delete_standard_size(id):
    standard_size = Standard_Size.query.get(id)
    if not standard_size:
        return {"SORRY":"Size not found."}
    
    db.session.delete(standard_size)
    #save changes in db
    db.session.commit()
    
    return {"NOTE":"This standard size has now been removed from the database successfully."}

@standard_size.route("/<int:id>", methods=["PUT"])
def update_standard_size(id):
    standard_size = Standard_Size.query.get(id)
    if not standard_size:
        return {"SORRY":"This standard size doesn't exist."}
    standard_size_fields = standard_size_schema.load(request.json)
    
    standard_size.name = standard_size_fields["name"]
    standard_size.clothing_size = standard_size_fields["clothing_size"]
    standard_size.shoe_size = standard_size_fields["shoe_size"]
    
    db.session.commit()
    
    return(standard_size_schema.dump(standard_size)), 201

@standard_size.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400
