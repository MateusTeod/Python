from flask import Flask, render_template, url_for, session, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import urllib.parse

#Configurações de conexão com SQL Server
params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=RochaFitnessDB;"
   "Trusted_Connection=yes;"
 )

app = Flask(__name__)
app.secret_key = 'MateusTeod' 
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'senha' not in data:
        return jsonify({"error": "Dados inválidos"}), 400
    
    email = data['Email']
    senha = data['Senha']

    




if __name__ == '__main__':
    app.run(debug=True)