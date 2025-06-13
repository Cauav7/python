def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(raio, PI):
    return 2 * PI * raio

def calculaArea(raio, PI):
    return PI * (raio ** 2)

#main
raio = int(input("Escreva o raio da circunferência (inteiro): "))
PI = 3.14159
diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(raio, PI)
area = calculaArea(raio, PI)
print("Diametro: ", diametro)
print("Circunferencia: ", circunferencia)
print("Área: ", area)