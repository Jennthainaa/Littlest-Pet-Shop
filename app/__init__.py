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

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    from .payment import payment as payment_blueprint
    app.register_blueprint(payment_blueprint, url_prefix='/payment')




    from .import routes
    routes.init_app(app)
    return app