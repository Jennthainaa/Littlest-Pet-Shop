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
    
    from .pets import pets as pets_blueprint
    app.register_blueprint(pets_blueprint, url_prefix='/pets')


    from .import routes
    routes.init_app(app)
    return app