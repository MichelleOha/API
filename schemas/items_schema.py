from main import ma

class ItemSchema(ma.Schema):
    class Meta:
        #ordered = True
        fields = ["item_id", "description", "style", "size", "price", "season", "brand_name"]
        
#single item schema
item_schema = ItemSchema()
#multiple schemas
items_schema = ItemSchema(many=True)
