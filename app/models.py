from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # def _repr_(self):
    #     return f'<Usuario {self.username}, Email:{self.email}>'
    
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relação de um Pet com o Usuário
    # usuario = db.relationship('Usuario', backref=db.backref('pets', lazy=True))

    # def __repr__(self):
    #     return f'<Pet {self.nome}, Espécie:{self.especie}, Idade:{self.idade}>'
class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data_venda = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pet = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    id_servico = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)
    data_agendamento = db.Column(db.Date, nullable=False)
    hora_agendamento = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50))

    # pet = db.relationship('Pet', backref=db.backref('agendamentos', lazy=True))
    # servico = db.relationship('Servico', backref=db.backref('agendamentos', lazy=True))

    # Relação com o User
   # usuario = db.relationship('User', backref=db.backref('vendas', lazy=True))
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descri_prod = db.Column(db.String(255))
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)

    # Métodos auxiliares para gestão de estoque (opcional)
    # def atualizar_estoque(self, quantidade):
    #     if quantidade < 0 and abs(quantidade) > self.qtd_estoque:
    #         raise ValueError("Quantidade insuficiente no estoque")
    #     self.qtd_estoque += quantidade

    # def __repr__(self):
    #     return f"<Produto {self.nome}, Valor: {self.valor}, Estoque: {self.qtd_estoque}>"
# class pagamento(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # Identificador único para o pagamento
#     id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # FK para usuário
#     id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)  # FK para endereço
#     forma_pagamento = db.Column(db.String(50), nullable=False)  # Forma de pagamento (ex.: cartão, PIX)
#     valor_pagamento = db.Column(db.Numeric(10, 2), nullable=False)  # Valor total do pagamento
#     detalhes_pagamento = db.Column(db.String(255))  # Detalhes adicionais do pagamento
class payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(255))
    cep = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    frete = db.Column(db.String(50), nullable=False)
    pagamento = db.Column(db.String(50), nullable=False)


    from app import db




