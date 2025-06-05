import os
import json

# Arquivos externos para armazenar dados
USERS_FILE = 'users.json'
STOCK_FILE = 'stock.json'

# Funções auxiliares para manipular arquivos JSON
def load_data(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({}, f)
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

# Funções para gerenciar usuários
def cadastrar_usuario():
    users = load_data(USERS_FILE)
    name = input('Digite o nome do usuário: ').strip()
    email = input('Digite o email do usuário: ').strip()
    if not name or not email:
        print('Nome ou email inválido.')
        return
    users[email] = {'nome': name}
    save_data(USERS_FILE, users)
    print(f'Usuário {name} cadastrado com sucesso!')

def editar_usuario():
    users = load_data(USERS_FILE)
    email = input('Digite o email do usuário que deseja editar: ').strip()
    if email not in users:
        print('Usuário não encontrado.')
        return
    name = input('Digite o novo nome do usuário: ').strip()
    users[email]['nome'] = name
    save_data(USERS_FILE, users)
    print(f'Usuário {email} atualizado com sucesso!')

def excluir_usuario():
    users = load_data(USERS_FILE)
    email = input('Digite o email do usuário que deseja excluir: ').strip()
    if email not in users:
        print('Usuário não encontrado.')
        return
    del users[email]
    save_data(USERS_FILE, users)
    print(f'Usuário {email} excluído com sucesso!')

def gerenciar_usuarios():
    while True:
        print('------ Menu Usuários ------')
        print('1. Cadastrar usuário')
        print('2. Editar usuário')
        print('3. Excluir usuário')
        print('0. Voltar')
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            editar_usuario()
        elif opcao == '3':
            excluir_usuario()
        elif opcao == '0':
            break
        else:
            print('Opção inválida.')

# Funções para gerenciar estoque
def adicionar_estoque():
    stock = load_data(STOCK_FILE)
    produto = input('Digite o nome do produto: ').strip()
    quantidade = input('Digite a quantidade: ').strip()
    if not produto or not quantidade.isdigit():
        print('Dados inválidos.')
        return
    stock[produto] = stock.get(produto, 0) + int(quantidade)
    save_data(STOCK_FILE, stock)
    print(f'Produto {produto} atualizado com sucesso!')

def editar_estoque():
    stock = load_data(STOCK_FILE)
    produto = input('Digite o nome do produto que deseja editar: ').strip()
    if produto not in stock:
        print('Produto não encontrado.')
        return
    quantidade = input('Digite a nova quantidade: ').strip()
    if not quantidade.isdigit():
        print('Quantidade inválida.')
        return
    stock[produto] = int(quantidade)
    save_data(STOCK_FILE, stock)
    print(f'Produto {produto} atualizado com sucesso!')

def excluir_estoque():
    stock = load_data(STOCK_FILE)
    produto = input('Digite o nome do produto que deseja excluir: ').strip()
    if produto not in stock:
        print('Produto não encontrado.')
        return
    del stock[produto]
    save_data(STOCK_FILE, stock)
    print(f'Produto {produto} excluído com sucesso!')

def gerenciar_estoque():
    while True:
        print('------ Menu Estoque ------')
        print('1. Adicionar produto')
        print('2. Listar produtos')
        print('3. Editar produto')
        print('4. Excluir produto')
        print('0. Voltar')
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            adicionar_estoque()
        elif opcao == '2':
            stock = load_data(STOCK_FILE)
            if not stock:
                print('Estoque vazio.')
            else:
                print('Produtos no estoque:')
                for produto, quantidade in stock.items():
                    os.system('cls')
                    print(f'{produto}: {quantidade}')
                os.system('pause')
                os.system('cls')
        elif opcao == '2':
            editar_estoque()
        elif opcao == '3':
            excluir_estoque()
        elif opcao == '0':
            break
        else:
            print('Opção inválida.')

# Menu principal
def menu_principal():
    while True:
        print('------ Menu Principal ------')
        print('1. Gerenciar usuários')
        print('2. Gerenciar estoque')
        print('0. Sair')
        opcao = input('Escolha uma opção: ').strip()
        if opcao == '1':
            gerenciar_usuarios()
        elif opcao == '2':
            gerenciar_estoque()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

# Login inicial
def login():
    print('--- BEM-VINDO AO SISTEMA ---')
    user = input('Login: ').strip()
    password = input('Senha: ').strip()
    if user == 'mateus' and password == '123':
        print(f'Login bem-sucedido! Bem-vindo {user}')
        os.system('pause')
        os.system('cls')
        menu_principal()
    else:
        print('Login ou senha incorretos.')

# Executar o sistema
login()