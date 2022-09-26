from unicodedata import name
from flask import Blueprint
from main import db
from main import bcrypt
from models.category import Category
from models.items import Items
from models.size import Size
from models.users import Users
from models.receipt import Receipt

# from symbol import yield_arg

#create blueprint
db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')
    
@db_commands.cli.command('seed')
def seed_db():
    user1 = Users(
        username = "Aimee",
        email = "aimee@email.com",
        password = bcrypt.generate_password_hash("password").decode("utf-8")
    )
    
    db.session.add(user1)
    
    user2 = Users(
        username = "Jacob",
        email = "jacob@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    
    db.session.add(user2)
    
    item1 = Items(
        description = "Boyfriend jeans",
        style = "pants",
        size = "12",
        price = 299.00,
        season = "winter",
        brand_name = "Nobody"
    )
    
    db.session.add(item1)
    
    category1 = Category(
        type = "Womens wear"
    )
    
    db.session.add(category1)
    
    category2 = Category(
        type = "Mens wear"
    )
    
    db.session.add(category2)
    
    category3 = Category(
        type = "Childrens wear"
    )
    
    db.session.add(category3)
    
    category4 = Category(
        type = "Footwear"
    )
    
    db.session.add(category4)
    
    category5 = Category(
        type = "Underwear"
    )
    
    db.session.add(category5)
    
    category6 = Category(
        type = "swimwear"
    )
    
    db.session.add(category6)
    
    
    receipt1 = Receipt(
       online_or_instore = "online",
       year = 2022,
       store = "Net-a-porter"
   )
    
    db.session.add(receipt1)
    
    size4 = Size (
        name = "Lachie",
        clothing_size = "8",
        shoe_size = 9
    )
    
    db.session.add(size4)
    
    db.session.commit()
    print("Tables seeded")
    
    
    
    
    
    
    
        
    
    