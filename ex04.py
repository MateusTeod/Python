entrada = input('Digite que horas são em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora !')
except:
    print('Por favor, digite somente números inteiros !')