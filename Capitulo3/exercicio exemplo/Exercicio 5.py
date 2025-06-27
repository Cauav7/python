def right_justify(palavra, tamanhoPalavra):
    espaco = ' '
    resultado = espaco * (70 - tamanhoPalavra)
    return resultado + palavra

palavra = str(input("Digite uma palavra:"))
tamanhoPalavra = len(palavra)

justificado = right_justify(palavra, tamanhoPalavra) # chamada de funcao recebe argumento

print(justificado)