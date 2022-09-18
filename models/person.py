from main import db

class Person(db.Model):
    #define the tablename in the database
    __tablename__ = "person"
    #setting the columns
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    clothing_size = db.Column(db.String(20))
    shoe_size = db.Column(db.Float)
    
    