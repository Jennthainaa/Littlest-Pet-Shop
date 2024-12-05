from flask import render_template
from .import users

@users.route('/')
def index():
    return render_template('users/index.html')

