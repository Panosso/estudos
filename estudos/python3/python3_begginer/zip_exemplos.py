#syntax: zip(lista1, lista2...listaN)

lista = [1,2,3,4,5,6,7]
lista2 = [1,2,3,4,5,6,7,10,20,30]
lista3 = [1,2,3,4,5,6,7,10,20,30,40,50]

print(list(zip(lista2, lista, lista3)))
#saida: [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7)]

dic1 = {'a':1, 'b':2}
dic2 = {'c':3, 'd':4}

#Combinando chave e valor dos 2 dic
print(list(zip(dic1.items(), dic2.items())))

#Combinando valor dos 2 dic
print(list(zip(dic1.values(), dic2.values())))
