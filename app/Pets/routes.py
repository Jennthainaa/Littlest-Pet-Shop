from flask import render_template
from .import pets

@pets.route('/')
def index():
    return render_template('pets/index.html')