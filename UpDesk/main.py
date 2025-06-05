
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

usuarios = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com", "senha": "123456", "tipo": "usuario"},
    {"id": 2, "nome": "Maria Suporte", "email": "maria@email.com", "senha": "abc123", "tipo": "suporte_n1"}
]

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return jsonify({"mensagem": "Dados inválidos!"}), 400

    email = data.get('email')
    senha = data.get('senha')

    for usuario in usuarios:
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

if __name__ == '__main__':
    app.run(debug=True)