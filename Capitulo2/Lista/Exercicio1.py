#solicita ao usuario dois numero inteiros
print("Escreva dois numeros inteiros")
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

#Realiza as operacoes
soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2

#Cálculo do quociente com verificação de divisão por zero
if num2 != 0:
    quociente = num1 / num2
else:
    quociente = "indefinido (divisão por zero)"
# Exibe os resultados
print("\nResultados:")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Produto: {num1} * {num2} = {produto}")
print(f"Diferença: {num1} - {num2} = {diferenca}")
print(f"Quociente: {num1} / {num2} = {quociente}")