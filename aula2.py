'''num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
maior = num1 >= num2
menor = num1 <= num2
if num1 == maior:
    print('num1 é maior que o segundo valor')
elif num1 == menor:
    print('num1 é menor que o segundo valor')
if num2 == maior:
    print('num1 é maior que o segundo valor')
elif num2 == menor:
    print('num1 é menor que o segundo valor')'''

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}
    )
