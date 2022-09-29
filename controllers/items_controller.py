from cgi import print_exception
from crypt import methods
from tkinter.ttk import Style
from flask import Blueprint, request 
from main import db
from models.items import Items
from schemas.items_schema import item_schema, items_schema

items = Blueprint('items', __name__, url_prefix="/items")

@items.route("/", methods=["GET"])
def get_items():
    #get all the items from db
    items_list = Items.query.all()
    result = items_schema.dump(items_list)
    return(result) 

@items.route("/<int:id>", methods=["GET"])
def get_item(id):
    #get an item from db by id
    item = Items.query.get(id)
    result = item_schema.dump(item)
    return(result) 

@items.route("/", methods=["POST"])
def new_item():
    item_fields = item_schema.load(request.json)
    item = Items(
        description = item_fields["description"],
        style = item_fields["style"],
        size = item_fields["size"],
        price = item_fields["price"],
        season = item_fields["season"],
        brand_name = item_fields["brand_name"],
        standard_size_id = item_fields["standard_size_id"],
        category_id = item_fields["category_id"],
        users_id = item_fields["users_id"]
    )
    
    db.session.add(item)
    db.session.commit()
    return(item_schema.dump(item)) 

@items.route("/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Items.query.get(id)
    if not item:
        return {"SORRY":"item not found."}
    
    db.session.delete(item)
    #save changes in db
    db.session.commit()
    
    return {"NOTE":"The Item has now been removed from list successfully."}

@items.route("/<int:id>", methods=["PUT"]) #update_item
def update_item(id):
    item = Items.query.get(id)
    if not item:
        return {"SORRY":"This item doesn't exist."}
    item_fields = item_schema.load(request.json)
    
    item.description = item_fields["description"]
    item.style = item_fields["style"]
    item.size = item_fields["size"]
    item.price = item_fields["price"]
    item.season = item_fields["season"]
    item.brand_name = item_fields["brand_name"]
    
    
    db.session.commit()
    
    return(item_schema.dump(item))