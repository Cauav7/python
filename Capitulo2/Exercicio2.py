percoCapa = 24.95
descontoLivraria = percoCapa * 0.40
precodeCapaLivraria = percoCapa - descontoLivraria

fretePrimeiroExemplar = 3.00
freteRestanteExemplar = 0.75

custodeAtacadodoprimeiroExemplar = precodeCapaLivraria + fretePrimeiroExemplar
custoAtacado = custodeAtacadodoprimeiroExemplar + ((precodeCapaLivraria + freteRestanteExemplar) * 59)

print("O custo total do atacado de 60 copias e de", custoAtacado)