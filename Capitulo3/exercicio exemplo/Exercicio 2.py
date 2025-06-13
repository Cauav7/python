def removerPrimeiroDigito(numero):
    return numero // 10000

def removerSegundoDigito(numero):
    return (numero % 10000) // 1000

def removerTerceiroDigito(numero):
    return (numero % 1000) // 100

def removerQuartoDigito(numero):
    return (numero % 100) // 10

def removerQuintoDigito(numero):
    return  (numero % 10)


#main
numero = int(input("Entre com um numero de 5 digitos:"))
primeiro_digito = removerPrimeiroDigito(numero)
segundo_digito = removerSegundoDigito(numero)
terceiro_digito = removerTerceiroDigito(numero)
quarto_digito = removerQuartoDigito(numero)
quinto_digito = removerQuintoDigito(numero)

print(primeiro_digito)
print(segundo_digito)
print(terceiro_digito)
print(quarto_digito)
print(quinto_digito)