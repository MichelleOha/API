from main import ma

class SizeSchema(ma.Schema):
    class Meta:
        fields = ["person_id", "name", "clothing_size", "shoe_size"]
        
#single schema
size_schema = SizeSchema()
#multiple schemas
sizes_schema = SizeSchema(many=True)
 