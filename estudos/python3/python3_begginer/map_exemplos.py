#syntax: map(funcao, lista)

def fare(temp):
    return temp**2

temp = lambda x: x**2

temp_lista = [1, 2, 3, 4]

print(temp(1))

#Passamdo a def
print(list(map(fare, temp_lista)))

#Passamdo a variavel temp que contem um lambda
print(list(map(temp, temp_lista)))

#Passando o lambda direto
print(list(map(lambda x: x**2, temp_lista)))

from math import pi

def area(r):
    """
        Calcula a area de um circulo
    """
    return pi * (r ** 2)

print(area(2))

raios = [1, 2, 3.5, 44, 6]

areas = map(area, raios)

print(map(area, raios))
print(list(map(area, raios)))
#Assim que imprimir as areas em forma de lista, ela será apagada da memória.
print(list(areas))

print("Areas")
#Ja nao existe mais a lista de areas
for i in areas:
    print("Areas")
    print(i)

print("Areas")

cidades = [('Rib preto', 12),('jaboticabal',19),('Sertaozinho',22),('matao',23),('cassia',11),('santo antonio',21),('Rei',31)]

c_pra_f = map((lambda dado: f'Cidade: {dado[0]}, Temperatura: {(dado[1] * 100)}'), cidades)

print(list(c_pra_f))
