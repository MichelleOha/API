from main import ma
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from models.items import Items
from models.users import Users 
# from schemas.items_schema import ItemSchema
# from schemas.users_schema import UsersSchema

class StandardSizeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["standard_size_id", "name", "clothing_size", "shoe_size", "users_id", "users", 
                  "item_id", "items"]
    # item = fields.Nested(ItemSchema, only = ["description", "brand_name"])
    # users = fields.Nested(UsersSchema, only = ["name"])
    item = fields.List(fields.Nested("ItemSchema", only=("description", "brand_name"))) 
    users = fields.List(fields.Nested("UsersSchema", only=("users_id", "username")))
    
#single schema
standard_size_schema = StandardSizeSchema()
#multiple schemas
standard_sizes_schema = StandardSizeSchema(many=True)
 