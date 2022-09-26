from main import db

class Category(db.Model):
    #define the tablename in the database
    __tablename__ = "Category"
    #setting the columns
    category_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(150))
    items = db.relationship(
        "Items",
        back_populate= "items"
    )
    
    
    
