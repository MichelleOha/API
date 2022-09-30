from main import db

class Items(db.Model):
    #define the tablename in the database
    __tablename__ = "items"
    #setting the columns
    item_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150))
    style = db.Column(db.String(150))
    size = db.Column(db.String(20))
    price = db.Column(db.Float)
    season = db.Column(db.String(20))
    brand_name = db.Column(db.String(150))
    standard_size_id = db.Column(db.Integer, db.ForeignKey("standard_size.standard_size_id"), nullable=False)
    # category_id = db.Column(db.String, db.ForeignKey('category.category_type'))
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.users_id"), nullable=False)
    receipt = db.relationship(
        "Receipt",
        backref= "items"
    )
#     category_type = db.relationship(
#     "Category",
#     backref="item_category_type"
#   )
    