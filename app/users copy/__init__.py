from flask import Blueprint

#cria o blueprint de users e especifica a pasta de templates
users = Blueprint('users', __name__, template_folder='templates')

from . import routes