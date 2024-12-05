from flask import Blueprint

#cria o blueprint de pets e especifica a pasta de templates
payment = Blueprint('payment', __name__, template_folder='templates')

from . import routes