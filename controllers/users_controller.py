from datetime import timedelta
from xml.dom import ValidationErr
from flask import Blueprint, request 
from main import db
from main import bcrypt
from main import jwt 
from flask_jwt_extended import create_access_token
from models.users import Users
from schemas.users_schema import user_schema
from marshmallow.exceptions import ValidationError


users = Blueprint('users', __name__, url_prefix="/users")

@users.route("/register", methods=["POST"])
def register_users():
    users_fields = user_schema.load(request.json)
    
    users = Users.query.filter_by(username=users_fields["username"]).first()
    if users:
        return{"SORRY":"This username already exists."}
    
    users = Users.query.filter_by(email=users_fields["email"]).first()
    if users:
        return{"SORRY":"This email already exists."}
    
    users = Users (
        username = users_fields["username"],
        email = users_fields["email"],
        password = bcrypt.generate_password_hash(users_fields["password"]).decode("utf-8")
    )
    
    db.session.add(users)
    db.session.commit()
    
    #gereanting the token setting the identity(users.id) and expiry time 
    token = create_access_token(identity=str(users.user_id), expires_delta=timedelta(days=10))
    
    return {"username":users.username, "token": token}

@users.route("/login", methods = ["post"])
def login_user():
    users_fields = user_schema.load(request.json)
    users = Users.query.filter_by(username=users_fields["username"]).first()
    if not users:
        return{"SORRY":"This username doesn't exist."}
    
    if not bcrypt.check_password_hash(users.passwords, users_fields["password"]):
        return{"SORRY":"This password is not correct."}
    
    token = create_access_token(identity=str(users.user_id), expires_delta=timedelta(days=10))
    
    return {"username":users.username, "token": token}

@users.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400
    
    
    
    
    
  

    