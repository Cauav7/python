print ('tempo do primeiro trecho')
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15

print("Tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3

print("Tempo do terceiro trecho: 8 min e 15 s")
minutoTerceiroTrecho = 8 * 60
segundosTerceiroTrecho = 15
#Soma o valor total de minutos e converte todos segundos em minutos
totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60
#Tem o valor total dos segundos
totalTempoTodosTrechosSegundos = (segundoPrimeiroTrecho + segundosSegundoTrecho + segundosTerceiroTrecho)

restamteMinutos = int(totalTempoTodosTrechosSegundos / 60)
restamteSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restamteMinutos
totalSegundos = restamteSegundos

print("Soma do tempo de todos os trechos", totalMinutos,
      "minutos")
print("Soma do tempo de todos os trechos", totalSegundos,
      "segundos")


horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos
print(horarioInicialSegundos)
print(minutoInicialSegundos)

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos)/60) %  60)
print("O tempo de chegada foi de ", horaChegada, ":", minutoChegada, restamteSegundos)