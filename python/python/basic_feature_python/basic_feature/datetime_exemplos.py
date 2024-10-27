import datetime

#Define a variavel t com 4horas 20minutos 1segundo e 10 microsegundos
t = datetime.time(4,20,1,10)

#Imprime apenas a hora
print(t.hour)

#Imprime apenas o minuto
print(t.minute)

#Imprime apenas o segundo
print(t.second)

#Imprime o microseundo
print(t.microsecond)

#Retornaria o time zone
print(t.tzinfo)

data_qualquer = datetime.datetime(2020, 10, 3, 10, 11, 30)

#Retorna de uma forma mais formata a variavel today
print(data_qualquer.ctime())

#Retorna o dia de hoje
print(datetime.date.today())

d1 = datetime.date(2015, 3, 11)
d2 = datetime.date(2016, 3, 11)

#Calcula a diferença de datas
print(d2 - d1)

#Converteando para um tipo de string mais amigavel
print(d1.strftime('%Y-%m-%d'))
