# main flask application code
 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy() #defining db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget_tracker.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all() #create database tables
    
    from .routes import setup_routes
    setup_routes(app)

    return app

