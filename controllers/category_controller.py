# from unicodedata import category
from flask import Blueprint
from main import db
from models.category import Category 

category = Blueprint('category', __name__, url_prefix="/category")

@category.route("/", methods=["GET"])
def get_category():
    #get all the category from db
    category_list = Category.query.all()
    
    return "list of Categories"