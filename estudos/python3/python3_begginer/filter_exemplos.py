#syntax: filter(funcao, lista)
lista = [1,2,3,4,5,6,7]

#Equivale a 'return x if x%2==0'
print(list(filter(lambda x: x%2==0, lista)))

musicas = [('Demons are girl', 100), ('Feijoada completa', 23), ('Macaos', 21), ('porto solidao', 31)]

maiores_musicas = filter((lambda musica: musica[1] > 22), musicas)

print(list(maiores_musicas))

paises_nulos = ['Chile','','','','','','Argentina','','Brasil']

paises = filter((lambda pais: len(pais) > 0), paises_nulos)

#Lembrando que None e '' são diferente o filter considera que uma string com o valor '' é para ser descartada.
paises = filter(None, paises_nulos)

print(list(paises))
