#syntax: reduce(funcao, lista)

#O reduce foi removido do python 3 por isso precisamos importar essa biblioteca
from functools import reduce

lista_numero = [1,2,3,4,5,6]

print(reduce(lambda x,y: x+y, lista_numero))
