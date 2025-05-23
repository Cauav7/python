numero = int(input("Digite um número de 5 dígitos: "))
digito1 = numero // 10000
digito2 = (numero % 10000) // 1000
digito3 = (numero % 1000) // 100
digito4 = (numero % 100) // 10
digito5 = numero % 10

print(digito1)
print(digito2)
print(digito3)
print(digito4)
print(digito5)