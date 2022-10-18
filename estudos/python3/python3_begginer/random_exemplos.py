from random import random, uniform, randint, choice, shuffle


#Nesse caso será gerado valore entre 0 e 1
for i in range(10):
    print(random())

#nesse caso será gerado valore no range determinado
for i in range(10):
    #Gera valores de 3 até 6.9999999999999999999, nunca chega no max do range
    print(uniform(3,7))

for i in range(10):
    #Gera numeros entre 1 e 60, não chega no max do range
    print(randint(1,61), end=', ')

jogadas = ['pedra', 'papel', 'tesoura']

#Retorna um dos valores da lista
print(choice(jogadas))

cartas = ['K', 'Q', 'J', 'A']

#Embaralha a lista
shuffle(cartas)

print(cartas)
