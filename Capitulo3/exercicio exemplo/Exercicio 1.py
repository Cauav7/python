from Capitulo1.Exemplo2operadoresaritimeticos import divisao


def soma(numero, numero2):
    print("O resultado da adicao é: ",numero + numero2)

def subtracao(numero, numero2):
    print("O resultado da subtracao é: ", numero - numero2)

def multiplicacao(numero, numero2):
    print("O resultado da multiplicacao é: ", numero * numero2)


    def divisao(numero, numero2):
    total_divisao = numero / numero2
    print("O resultado da divisao é: ", total_divisao)

numero = int(input("Digite o 1º numero:"))
numero2 = int(input("DIgite o 2º numero:"))


soma(numero, numero2)
subtracao(numero, numero2)
multiplicacao(numero, numero2)
divisao(numero, numero2)

