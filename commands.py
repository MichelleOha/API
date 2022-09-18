from flask import Blueprint
from main import db
from models.category import Category
from models.items import Items
from models.person import Person
from models.receipt import Receipt

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
    
    category1 = Category(
        type = "Womens wear"
    )
    
    db.session.add(category1)
    
    item1 = Items(
        description = "Boyfriend jeans",
        style = "pants",
        size = "12",
        price = 299.00,
        season = "winter",
        brand_name = "Nobody"
    )
    
    db.session.add(item1)
    
    db.session.commit()
    print("Tables seeded")
    
    
    
    
    
    
    
        
    
    