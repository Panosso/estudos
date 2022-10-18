my_list = [1, "abc", 2.3, True]

my_list2 = [1, "abc", 2.3, True]

my_list3 = ['a', 'b', 'x', 'c']

my_list5 = [2, 3, 4, 1, 5, 23, 5]

#adiciona um elemento
my_list.append("adicao permanente")

#retorna o tamanho da lista
print(len(my_list))

#remove um valor da lista
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)

#retorna a lista de forma reversa
for i in reversed(my_list5):
print(i)


#retorna a lista de forma ordenada
my_list4 = []
my_list4 = sorted(my_list3)
print(my_list4)

#Méodo extend, adiciona iteráveis na lista. Valores não podem ser adicionados.
my_list.extend(my_list2) #Vai adicionar todos os elementos da my_list2 no final do my_list
my_list.extend(43) #Vai dar erro

#Metodo clear, limpa a lista.
my_list.clear()

#Metodo copy, copia a lista
my_list5 = my_list.copy()

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]

matrix = [lista1, lista2, lista3]

print(matrix)
print(matrix[1])
print(matrix[1][2])

first_col = [row[0] for row in matrix]

print(first_col)

x = []

x = [i for i in range(0,10,1)]

print(x)

x.clear()

x = [i * 2 +10 for i in range(0,10,1)]

print(x)

x.clear()

x = [i for i in range(0, 20) if i % 2 == 0]

print(x)

x.clear()

x = [letter for letter in 'word' if letter != 'w']

print(x)

graus = [0, 10, 50, 100, 500]

far = [(temperatura * (9/5) + 32) for temperatura in graus]

print(far)

numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if not numero % 2]

impares = [numero for numero in numeros if numero % 2]

resultado = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

#listas aninhadas
listas = [[1,2,3],[4,5,6],[7,8,9]]

[[print(valor) for valor in lista] for lista in listas]

velha = [['O' if numero % 2 else 'X' for numero in range(1,4)] for linha in range(1,4)]

print(velha)
print(['O', 'X', 'O'] in velha)

print([[' ' for posicao in range(1,4)] for linha in range(1,4)])

lista = []

#Adiciona na lista
lista.append("A")
print(lista)

#Conta quantas vezes o elemento aparece na lista
print(lista.count('A'))

#extend: Quando passada uma lista, ele irá adicionar elemento por elemento na lista, ao inves de adicionar um novo elemento
# contendo a lista
lista.append([1,2,3,4])
print(lista)
lista.pop()
lista.extend([1,2,3,4])

print(lista)

#Retorna o elemento da lista
print(lista.index(2))

#Insere o segundo parametro na index colocado no primeiro parametro
lista.insert(2, 'Teste')
lista.insert(4, 'Teste')

print(lista)

#Remove a primeira aparicao do elemento, mantendo outras caso haja
lista.remove('Teste')
print(lista)
