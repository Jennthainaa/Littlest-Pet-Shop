from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


def init_app(app):
    @app.route('/')

    def index():
        return render_template('index.html')
     
        # @app.route('Cadastrar.html') 