from main import ma

class ReceiptSchema(ma.Schema):
    class Meta:
        fields = ["receipt_id", "online_or_instore", "year", "store"]
        
#single schema
receipt_schema = ReceiptSchema()
#multiple schemas
receipts_schema = ReceiptSchema(many=True)
 