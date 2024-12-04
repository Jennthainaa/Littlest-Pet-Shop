from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Stgring(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # def _repr_(self):
    #     return f'<Usuario {self.username}, Email:{self.email}>'
    
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    # Relação de um Pet com o Usuário
    # usuario = db.relationship('Usuario', backref=db.backref('pets', lazy=True))

    # def __repr__(self):
    #     return f'<Pet {self.nome}, Espécie:{self.especie}, Idade:{self.idade}>'

    from app import db




