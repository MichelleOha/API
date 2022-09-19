from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    #Create Flask app object
    app = Flask(__name__)

    app.config.from_object("config.app_config")
    
    db.init_app(app)
    ma.init_app(app)
  
  #register blueprint
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    from controllers import registerable_controllers
    for controller in registerable_controllers:
      app.register_blueprint(controller) 
    
    return app

