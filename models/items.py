from main import db

class Items(db.Model):
    #define the tablename in the database
    __tablename__ = "Items"
    #setting the columns
    item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150))
    style = db.Column(db.String(150))
    size = db.Column(db.String(20))
    price = db.Column(db.Float)
    season = db.Column(db.String(20))
    brand_name = db.Column(db.String(150))
    size_id = db.Column(db.Integer, db.ForeignKey("size.size_id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    receipt = db.relationship(
        "receipt",
        back_populate= "receipt"
    )