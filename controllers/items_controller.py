from cgi import print_exception
from tkinter.ttk import Style
from flask import Blueprint, request #removed jsonify
from main import db
from models.items import Items
from schemas.items_schema import item_schema, items_schema

items = Blueprint('items', __name__, url_prefix="/items")

@items.route("/", methods=["GET"])
def get_items():
    #get all the items from db
    items_list = Items.query.all()
    result = items_schema.dump(items_list)
    return(result) #removed jsonify

@items.route("/<int:id>", methods=["GET"])
def get_item(id):
    #get an item from db by id
    item = Items.query.get(id)
    result = item_schema.dump(item)
    return(result) #removed jsonify

@items.route("/", methods=["POST"])
def new_item():
    item_fields = item_schema(request.json)
    item = Items(
        description = item_fields["description"],
        style = item_fields["style"],
        size = item_fields["size"],
        price = item_fields["price"],
        season = item_fields["season"],
        brand_name = item_fields["brand_name"]
    )
    
    db.session.add(item)
    db.session.commit()
    return(item_schema.dump(item)) #removed jsonify