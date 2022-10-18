#Criando um set
#{1, 2, 3, 4, 5}
conjunto_set = set({4,5,1,2,3,4,4,4,4,41,2,True, 'abc'})

#Cria uma variavel set
x = set()

#Adiciona um valor ao set
x.add(1)
x.add(2)
#Esse numero nao sera adicionado, pq ele adiciona apenas valores unicos
x.add(1)
print(x)

#Aplicando set em uma lista
lista = [2,5,4,3,2,9,8,2,1,4,23,6,9,8,5,23,6]

#transforma a lista em set
lista_set = set(lista)

#printa os valores unicos e em ordem
print(lista_set)

#Define um set
s = set()
#Adiciona um valor em um set
s.add(1)
print(s)

#Limpa um set
s.clear()
print(s)

#Um set pode ser criado usando apenas chaves{}
sc = {1,2,3}
#Copia um set
s = sc.copy()
print(s)
s.add(4)
#Calcula a diferença entre os 2 sets
print(s.difference(sc))

s1 = {1,2,3}
s2 = {1,4,5}

#Calcula a diferenca e atribui para o s1
s1.difference_update(s2)
print(s1)

#Discarda o elemento, nao discarta o elemento que está no index 2, ele descarta o valor 2
s1.discard(2)
print(s1)

#Calcula a intersecçao do s1
s1 = {1,2,3}
s2 = {1,4,5}
s1.intersection_update(s2)
print(s1)

print(s1 & s2)
print(s1.intersection(s2))

#Calcula a uniao dos conjuntos
s1 = {1,2,3}
s2 = {1,4,5}
print(s1 | s2)
print(s1.union(s2))
print(s1)


conjunto_set = set({4,5,6,2,3})
conjunto_set2 = set({41,2,3})

#Retornará a soma dos 2 conjuntos
#{2, 3, 4, 5, 6, 41}
print(conjunto_set | conjunto_set2)
print(conjunto_set.union(conjunto_set2))

#Retornara a intersecção dos conjuntos
#{2, 3}
print(conjunto_set & conjunto_set2)
print(conjunto_set.intersection(conjunto_set2))

#Irá me retornar os valores que estão apenas no 'conjunto_set'
#{4, 5, 6}
print(conjunto_set.difference(conjunto_set2))

#declaração de um set
x = {1,2,3,4}

x = {x for x in range(4)}

print(x)

x = {x**2 for x in range(4)}

print(x)

print({letra for letra in 'Pedro Panosso'})
