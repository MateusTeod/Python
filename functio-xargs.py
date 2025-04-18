'''def soma(*numeros):
    resultado = 0 
    for num in numeros:
        resultado += num
    return resultado

x = soma (2,3,4,5)

print(x)
'''
def agencia (**carros):
    return carros

print(agencia(marca='gol', cor='Branca', motor =1.0, placa=1234))
print(agencia(marca='gol', cor='Preto', motor =1.6, placa=24444))
print(agencia(marca='gol', cor='vermelho', motor =1.0, placa=5564))