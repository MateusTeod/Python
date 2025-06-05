print("Qual e seu peso?")
peso = float(input())
print("Qual e sua altura?") 
altura = float(input())
imc = peso / (altura ** 2)
print("Seu IMC e: ", imc)
if imc < 18.5:
    print("Abaixo do peso") 
elif imc < 24.9:    
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
