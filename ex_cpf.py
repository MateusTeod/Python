#cpf_user = int(input('Digite seu CPF (SEM PONTO/ SEM TRACOS):'))
cpf = '74682489070'

nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
print((resultado * 10) % 11)

