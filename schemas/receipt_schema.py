from main import ma
from marshmallow import fields
from schemas.items_schema import ItemSchema
class ReceiptSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["receipt_id", "online_or_instore", "year", "store", "item_id", "item"]
        load_only = ['item_id']
    item = fields.Nested(ItemSchema, only = ["description", "brand_name"])
        
#single schema
receipt_schema = ReceiptSchema()
#multiple schemas
receipts_schema = ReceiptSchema(many=True)
 