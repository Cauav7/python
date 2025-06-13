def calculaIMC(peso, altura):
    return peso / (altura ** 2)

#main
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calculaIMC(peso, altura)

print("O seu imc é de: ", imc)