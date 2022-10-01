from flask import Blueprint, request
from main import db
from models.receipt import Receipt
from schemas.receipt_schema import receipt_schema, receipts_schema
from marshmallow.exceptions import ValidationError

receipt = Blueprint('receipt', __name__, url_prefix="/receipt")

@receipt.route("/", methods=["GET"])
def get_receipts():
    #get all the receipt from db
    receipts_list = Receipt.query.all()
    result = receipts_schema.dump(receipts_list)
    return(result), 200

  
@receipt.route("/<int:id>", methods=["GET"])
def get_receipt(id):
    #get an category from db by id
    receipt = Receipt.query.get(id)
    result = receipt_schema.dump(receipt)
    return(result), 200

@receipt.route("/", methods=["POST"])
def new_receipt():
    receipt_fields = receipt_schema.load(request.json)
    receipt = Receipt(
        online_or_instore = receipt_fields["online_or_instore"],
        year = receipt_fields["year"],
        store = receipt_fields["store"],
        items_id = receipt_fields["items_id"]
    )
    
    db.session.add(receipt)
    db.session.commit()
    return(receipt_schema.dump(receipt)), 201

@receipt.route("/<int:id>", methods=["DELETE"])
def delete_receipt(id):
    receipt = Receipt.query.get(id)
    if not receipt:
        return {"SORRY":"Receipt not found."}, 404
    
    db.session.delete(receipt)
    #save changes in db
    db.session.commit()
    
    return {"NOTE":"Receipt has now been removed from list successfully."}

@receipt.route("/<int:id>", methods=["PUT"]) #update_item
def update_receipt(id):
    receipt = Receipt.query.get(id)
    if not receipt:
        return {"SORRY":"This receipt doesn't exist."}
    receipt_fields = receipt_schema.load(request.json)
    
    receipt.type = receipt_fields["type"]

    db.session.commit()
    
    return(receipt_schema.dump(receipt)), 201

@receipt.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400