'''num1 = input('Digite um número INTEIRO: ')

if num1 == float:
    print('Esse número nao é inteiro !')

if num1 % 2 == 0:
    print ('Esse número é par !')
else:
    print ('Esse número é ímpar !')
'''
entrada = input('Digite um número: ')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


