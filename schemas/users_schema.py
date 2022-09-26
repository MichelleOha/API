from wsgiref import validate
from main import ma
from marshmallow.validate import Length

from models.users import Users

class UsersSchema(ma.Schema):
    class Meta:
        fields = ("users_id", "username", "email", "password")
    #add validation to password
    username = ma.String(required = True)
    email = ma.String(required = True)
    password = ma.String(validate=Length(min=6))

user_schema = UsersSchema()
#multiple schema not necessary right now
users_schema = UsersSchema(many=True)

