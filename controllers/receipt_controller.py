from flask import Blueprint
from main import db
from models.receipt import Receipt

receipt = Blueprint('receipt', __name__, url_prefix="/receipt")

@receipt.route("/", methods=["GET"])
def get_receipt():
    #get all the receipt from db
    receipt_list = Receipt.query.all()
    
    return "list of receipts"