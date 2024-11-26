from flask import FLask
from config import Config

def create_app():
    app = FLask(__name__)

    from .import routes
    routes.init_app(app)
    return app
