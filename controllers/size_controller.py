from flask import Blueprint, request
from main import db
from models.size import Size
from schemas.size_schema import size_schema, sizes_schema

size = Blueprint('size', __name__, url_prefix="/size")

@size.route("/", methods=["GET"])
def get_sizes():
    #get all the person from db
    sizes_list = Size.query.all()
    result = sizes_schema.dump(sizes_list)
    return(result)

@size.route("/<int:id>", methods=["GET"])
def get_size(id):
    #get an item from db by id
    size = Size.query.get(id)
    if not size:
        return {"SORRY": "This size id doesn't exist."}
    result = size_schema.dump(size)
    return(result) 

@size.route("/", methods=["POST"])
def create_size():
    size_fields = size_schema.load(request.json)
    size = Size (
        name = size_fields["name"],
        clothing_size = size_fields["clothing_size"],
        shoe_size = size_fields["shoe_size"],
    )
    
    db.session.add(size)
    db.session.commit()
    return(size_schema.dump(size))

@size.route("/<int:id>", methods=["DELETE"])
def delete_size(id):
    size = Size.query.get(id)
    if not size:
        return {"SORRY":"Size not found."}
    
    db.session.delete(size)
    #save changes in db
    db.session.commit()
    
    return {"NOTE":"This size has now been removed from the database successfully."}

@size.route("/<int:id>", methods=["PUT"])
def update_size(id):
    size = Size.query.get(id)
    if not size:
        return {"SORRY":"This size doesn't exist."}
    size_fields = size_schema.load(request.json)
    
    size.name = size_fields["name"]
    size.clothing_size = size_fields["clothing_size"]
    size.shoe_size = size_fields["shoe_size"]
    
    db.session.commit()
    
    return(size_schema.dump(size))


