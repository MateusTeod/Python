altura = int(input('Qual altura da parede? '))
largura = int(input('Qual a largura da parede? '))
lata = int(input('Qual o redimento da lata de tinta? '))

def calcular_tinta ():
    area = altura * largura 
    redimento = area/ lata
    print(f'Voce precisa de {redimento} latas de tinta')

calcular_tinta()