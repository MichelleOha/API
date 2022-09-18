from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #Create Flask app object
    app = Flask(__name__)

    app.config.from_object("config.app_config")
    
    db.init_app(app)
  
  #register blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    return app

