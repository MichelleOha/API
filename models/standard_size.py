from main import db

class Standard_Size(db.Model):
    #define the tablename in the database
    __tablename__ = "standard_size"
    #setting the columns
    standard_size_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    clothing_size = db.Column(db.String(20))
    shoe_size = db.Column(db.Float)
    users_id = db.Column(db.Integer, db.ForeignKey("users.users_id"))
    # item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    
    items = db.relationship(
        "Items",#class
        backref= "standard_size",
        cascade= "all, delete"
    )
    
    
    
    