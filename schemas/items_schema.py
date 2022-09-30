from main import ma
from marshmallow import fields
from schemas.standard_size_schema import StandardSizeSchema
from schemas.category_schema import CategorySchema
from schemas.users_schema import UsersSchema

class ItemSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["item_id", "description", "style", "size", "price", "season", "brand_name", "standard_size_id", 
                 "category_id", "users_id"]
        load_only = ['standard_size_id', 'category_id']
    standard_size = fields.Nested(StandardSizeSchema, only=("clothing_size", "shoe_size",))
    category = fields.Nested(CategorySchema, only=("type",))   #ields.Pluck(CategorySchema, "category", many=False) #fields.Nested(CategorySchema, only=("type")) 
    users = fields.Nested("UsersSchema", only=("username",))
    # fields.List(fields.Nested("UsersSchema", only=("username",)))
    
        
#single item schema
item_schema = ItemSchema()
#multiple schemas
items_schema = ItemSchema(many=True)
