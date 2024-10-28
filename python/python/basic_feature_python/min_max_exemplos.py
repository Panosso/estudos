tupla = (3,4,5,6,2,7,1,2,7)

lista = [3,4,5,6,2,7,1,2,7]

my_dic = {'a': 123, 'b': 6, 'c': 5, 'd': 4,'e': 3, 'f': 2, 'g': 1}

val1 = 10
val2 = 12

nomes = ['Pedro', 'Yago', 'Jaque', 'Claudio', 'zAustraloptecos']

musicas = [{"titulo": "Thunder", "tocou":4},
        {"titulo": "Dead skin mask", "tocou":2},
        {"titulo": "back in black", "tocou":3},
        {"titulo": "Too old to rock n' roll", "tocou":7}]
        
#Rertorna o maior valor
print(max(tupla))

#retorna a maior chave do dicionario
print(max(my_dic))

#retorna o maior valor do dicionario
print(max(my_dic.values()))


#Retorna o maior dos 2 valores
print(max(val1, val2))


#Retorna o menor valor
print(max(tupla))

#retorna a menor chave do dicionario
print(max(my_dic))

#retorna o menor valor do dicionario
print(max(my_dic.values()))


#Retorna o menor dos 2 valores
print(max(val1, val2))

#Segue a ordem alfabética
print(max(nomes))
print(min(nomes))

#Alterando a key de filtro
print(max(nomes, key=lambda nome: len(nome)))

#Filtrando pelo parametro tocou
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
