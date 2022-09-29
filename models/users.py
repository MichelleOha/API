from main import db

class Users(db.Model):
    __tablename__ = "users"

    users_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    items = db.relationship(
        "Items",
        backref= "users"
    )
    standard_size = db.relationship(
        "Standard_Size",
        backref= "users"
    )
    