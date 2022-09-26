from main import ma

class CategorySchema(ma.Schema):
    class Meta:
        fields = ["category_id", "type"]
        
#single schema
category_schema = CategorySchema()
#multiple schemas
categories_schema = CategorySchema(many=True)
 