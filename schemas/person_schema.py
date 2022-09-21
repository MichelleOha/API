from main import ma

class PersonSchema(ma.Schema):
    class Meta:
        fields = ["person_id", "name", "clothing_size", "shoe_size"]
        
#single schema
person_schema = PersonSchema()
#multiple schemas
persons_schema = PersonSchema(many=True)
 