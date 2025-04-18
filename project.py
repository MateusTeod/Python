import os


print('---BEM-VINDO AO SISTEMA---')


user = str(input('Login: '))
password = int(input('Senha: '))

if user == 'mateus' and password == 123:
    print(f'Login bem-sucedido! Bem-vindo {user}' )
    os.system('pause')
    os.system('cls')
else:
    print('Login/senha incorreta')
    #for password in range(3):
    #    int(input('Senha: '))


def gerUser():
    print('------menu------')
    print('Escolha uma da opçoes abaixo:\n')
    print('1.cadastrar usuario.\n')
    print('2.Alterar usuario.\n')
    print('3.Desablitar usuario.\n')
    print('0.Voltar.\n')


def opcoesMa():
    print('-----MENU------')
    print('Escolha uma da opçoes abaixo:\n')
    print('1.Gerenciar usuario\n')
    print('2.Acessar estoque\n')
    print('3.Vender\n')
    print('0.Sair')


opcoesMa()

opcoes = int(input('Escolha uma opcao: '))

match opcoes:
    case 1:
        gerUser()
        os.system('cls')
    case 2:
        print('Acessar estoque')
    case 3:
        print('Vender')
    case 0:
        opcoesMa()
        os.system('cls')
    case _:
        print('Opção inválida')



int(input('Escolha uma opcao:'))


