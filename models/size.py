from main import db

class Size(db.Model):
    #define the tablename in the database
    __tablename__ = "size"
    #setting the columns
    size_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    clothing_size = db.Column(db.String(20))
    shoe_size = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    items = db.relationship(
        "Items",
        back_populate= "items"
    )
    