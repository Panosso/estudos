nomes = ['Pedro', 'Yago', 'Jaque', 'Claudio', 'Australoptecos']

musicas = [{"titulo": "Thunder", "tocou":4},
        {"titulo": "Dead skin mask", "tocou":2},
        {"titulo": "back in black", "tocou":3},
        {"titulo": "Too old to rock n' roll", "tocou":7}]

#Retorna um list_reverseiterator
print(reversed(nomes))

#Necessário converte-lo para o que precisar.
print(tuple(reversed(nomes)))
print(list(reversed(nomes)))
print(set(reversed(nomes)))
