from collections import Counter

lista = [1,2,1,4,1,3,4,8,7,4,5,2,1,4,56,6,8,7,1,2,5,8]


print(Counter(lista))
#Counter({1: 5, 4: 4, 2: 3, 8: 3, 7: 2, 5: 2, 3: 1, 56: 1, 6: 1})

print(Counter("abcdedadscdefresadsacxcxzsfe"))
#Counter({'d': 5, 'a': 4, 'c': 4, 'e': 4, 's': 4, 'f': 2, 'x': 2, 'b': 1, 'r': 1, 'z': 1})

s = "Quantas palavras que tem nessa frase formada por palavras"

c = Counter(s.split())

juncao = zip(c, lista)


print(c)
#Counter({'palavras': 2, 'Quantas': 1, 'tem': 1, 'nessa': 1, 'frase': 1, 'formada': 1, 'por': 1, 'palvras': 1, 'e': 1, 'nada': 1, 'de': 1, 'numero': 1, 'ou': 1, 'outra': 1, 'coisa': 1, 'que': 1, 'nao': 1, 'sejam': 1})

#Se for passado um parametro numero x, será retornado os x primeiros 'most common'
print(c.most_common())
#[('palavras', 3), ('que', 2), ('Quantas', 1), ('tem', 1), ('nessa', 1), ('frase', 1), ('formada', 1), ('por', 1), ('e', 1), ('nada', 1), ('de', 1), ('numero', 1), ('ou', 1), ('outra', 1), ('coisa', 1), ('nao', 1), ('sejam', 1)]


# Total de contagens
print(c.values())

# soma o total de todas as contagens
print(sum(c.values()))

#Transforma a contagem em lista
print(list(c))

#Converte para um conjunto
print(set(c))

#Converte para um dicionario
print(dict(c))

#Converte para uma lista de pares (elem, quantidade)
print(c.items())

#Counter(dict(list_of_pairs))    # converter de uma lista de pares (elem, cnt)
print(Counter(dict(juncao)))

#Limpa a contagem
print(c.clear())
