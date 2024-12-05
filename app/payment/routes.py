from flask import render_template, request, redirect, url_for, flash
from . import payment
from app import db
from app.models import payment

@payment.route('/')
def index():
    return render_template('payment/index.html')

# @payment.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # Captura os dados do formulário
#         id_usuario = request.form.get('id_usuario')  # Suponha que você tenha o ID do usuário em um campo oculto ou sessão
#         id_endereco = request.form.get('id_endereco')  # Suponha que você tenha o ID do endereço
#         forma_pagamento = request.form.get('forma_pagamento')
#         valor_pagamento = request.form.get('valor_pagamento')
#         detalhes_pagamento = request.form.get('detalhes_pagamento')

#         # Cria uma nova entrada de pagamento
#         novo_pagamento = pagamento(
#             id_usuario=id_usuario,
#             id_endereco=id_endereco,
#             forma_pagamento=forma_pagamento,
#             valor_pagamento=valor_pagamento,
#             detalhes_pagamento=detalhes_pagamento
#         )

#         # Adiciona o pagamento ao banco de dados
#         db.session.add(novo_pagamento)
#         db.session.commit()

#         flash('Pagamento realizado com sucesso!', 'success')
#         return redirect(url_for('payment.home'))  # Redireciona para a tela principal após o pagamento

#     return render_template('index.html')  # Renderiza a página inicial com o formulário de pagamento

# @pagamento.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # Captura de todos os campos do formulário
#         nome = request.form.get('nome')
#         sobrenome = request.form.get('sobrenome')
#         cpf = request.form.get('cpf')
#         celular = request.form.get('celular')
#         email = request.form.get('email')
#         endereco = request.form.get('endereco')
#         numero = request.form.get('numero')
#         complemento = request.form.get('complemento')
#         cep = request.form.get('cep')
#         cidade = request.form.get('cidade')
#         estado = request.form.get('estado')
#         frete = request.form.get('frete')
#         pagamento = request.form.get('pagamento')

#         # Criando uma nova instância do modelo Pedido
#         novo_pedido = pagamento(
#             nome=nome,
#             sobrenome=sobrenome,
#             cpf=cpf,
#             celular=celular,
#             email=email,
#             endereco=endereco,
#             numero=numero,
#             complemento=complemento,
#             cep=cep,
#             cidade=cidade,
#             estado=estado,
#             frete=frete,
#             pagamento=pagamento
#         )

#         # Adicionando o pedido no banco de dados
#         db.session.add(novo_pedido)
#         db.session.commit()

#         # Retornar uma resposta de sucesso ou redirecionar para outra página
#         return f"Pedido realizado com sucesso para {nome} {sobrenome}!"

#     return render_template('checkout.html')

# @payment.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         # Captura de todos os campos do formulário
#         nome = request.form.get('nome')
#         sobrenome = request.form.get('sobrenome')
#         cpf = request.form.get('cpf')
#         celular = request.form.get('celular')
#         email = request.form.get('email')
#         endereco = request.form.get('endereco')
#         numero = request.form.get('numero')
#         complemento = request.form.get('complemento')
#         cep = request.form.get('cep')
#         cidade = request.form.get('cidade')
#         estado = request.form.get('estado')
#         frete = request.form.get('frete')
#         pagamento = request.form.get('pagamento')

#         # Retorne todos os dados recebidos
#         return f"""
#             Dados recebidos:<br>
#             Nome: {nome}<br>
#             Sobrenome: {sobrenome}<br>
#             CPF: {cpf}<br>
#             Celular: {celular}<br>
#             E-mail: {email}<br>
#             Endereço: {endereco}<br>
#             Número: {numero}<br>
#             Complemento: {complemento}<br>
#             CEP: {cep}<br>
#             Cidade: {cidade}<br>
#             Estado: {estado}<br>
#             Frete: {frete}<br>
#             Pagamento: {pagamento}
#         """
#     return render_template('checkout.html')
