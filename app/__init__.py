from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #inicializa o db com o app
    db.init_app(app)
    migrate.init_app(app,db)
    
    from .import routes
    routes.init_app(app)
    return app