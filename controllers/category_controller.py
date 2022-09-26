# from unicodedata import category
from main import db
from models.category import Category 
from flask import Blueprint, request 
from schemas.category_schema import category_schema, categories_schema

category = Blueprint('category', __name__, url_prefix="/category")

@category.route("/", methods=["GET"])
def get_categories():
    #get all the category from db
    categories_list = Category.query.all()
    result = categories_schema.dump(categories_list)
    return(result) 


@category.route("/<int:id>", methods=["GET"])
def get_category(id):
    #get an category from db by id
    category = Category.query.get(id)
    result = category_schema.dump(category)
    return(result) 

@category.route("/", methods=["POST"])
def new_category():
    category_fields = category_schema.load(request.json)
    category = Category(
        type = category_fields["type"]
    )
    
    db.session.add(category)
    db.session.commit()
    return(category_schema.dump(category)) 

@category.route("/<int:id>", methods=["DELETE"])
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return {"SORRY":"category not found."}
    
    db.session.delete(category)
    #save changes in db
    db.session.commit()
    
    return {"NOTE":"The category has now been removed from list successfully."}

@category.route("/<int:id>", methods=["PUT"]) #update_item
def update_category(id):
    category = Category.query.get(id)
    if not category:
        return {"SORRY":"This category doesn't exist."}
    category_fields = category_schema.load(request.json)
    
    category.type = category_fields["type"]

    db.session.commit()
    
    return(category_schema.dump(category))