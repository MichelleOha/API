from main import db

class Receipt(db.Model):
    #define the tablename in the database
    __tablename__ = "receipt"
    #setting the columns
    receipt_id = db.Column(db.Integer, primary_key=True)
    online_or_instore = db.Column(db.String(10))
    year = db.Column(db.Integer)
    store = db.Column(db.String(100))
    