
from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import create_engine 


# banco de dados fictício
usuarios = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com", "senha": "123456", "tipo": "usuario"},
    {"id": 2, "nome": "Maria Suporte", "email": "maria@email.com", "senha": "abc123", "tipo": "suporte_n1"}
]

chamados = [] # lista de chamados vazia

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json # obtém os dados do JSON enviado no corpo da requisição
    if not data: # verifica se os dados estão vazios
        return jsonify({"mensagem": "Dados inválidos!"}), 400

    email = data.get('email')
    senha = data.get('senha')

    for usuario in usuarios:   # percorre a lista de usuários (verifica se o email e a senha correspondem a um usuário)
        if usuario['email'] == email and usuario['senha'] == senha:
            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "usuario": {
                    "id": usuario["id"],
                    "nome": usuario["nome"],
                    "tipo": usuario["tipo"]
                }
            }), 200

    return jsonify({"mensagem": "Email ou senha inválidos!"}), 401

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chamado')
def chamado():
    return render_template('chamado.html')

@app.route('/chamado', methods=['POST'])
def abrir_chamado():
    data = request.json
    if not data:
        return jsonify({"mensagem": "Dados inválidos!"}), 400
    
    # insere um novo chamado na lista de chamados
    chamado = {
        "id": len(chamados) + 1,
        "titulo": data.get("titulo"),
        "descricao": data.get("descricao"),
        "status": "aberto",
        "usuario_id": data.get("usuario_id"),
        "data-criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    chamados.append(chamado)
    return jsonify({"mensagem": "Chamado criado com sucesso!", "chamado": chamado}), 201

@app.route('/ver-chamado')
def ver_chamado():
    return render_template('Verchamado.html')



if __name__ == '__main__':
    app.run(debug=True)