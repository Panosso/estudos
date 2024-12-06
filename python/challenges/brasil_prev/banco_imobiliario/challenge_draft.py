from csv import writer
from random import randint

from player import Player

list_dict_test = [{1: 'a'}, {2: 'b'}]

print(len(list_dict_test))

quadrant = 300

quadrant1 = round(quadrant * 0.22)
quadrant2 = round(quadrant * 0.13)
quadrant3 = round(quadrant * 0.40)
quadrant4 = round(quadrant * 0.07)
quadrant5 = round(quadrant * 0.18)

print(quadrant1)
print(quadrant2)
print(quadrant3)
print(quadrant4)
print(quadrant5)

locations = ['Eiffel Tower', 'Choperia Pinguim', 'Museum Louvre',
             'Epcot Center', 'Beto Carreiro World',
             'Tulemar Bungalows & Villas', 'Hotel Jeri',
             'Magic Kingdom', 'Animal Kingdom',
             'Disney Hollywood', 'Vassoura Quebrada',
             'Taverna Medieval', 'Viking Axes Brasil',
             'Kongo Pizzaria', 'Jurassic Park Burger', 'Katon',
             'Fast Escova', 'Areia que canta', 'Pousada', 'Vivenda']

print(locations[randint(0, len(locations))])

location = locations[randint(0, len(locations))]

print(location)

locations.pop(locations.index(location))

locations.pop(locations.index(locations[0]))

print(locations)

impulsive_player = Player('Impulsive', 'Compra qualquer propriedade')
demanding_player = Player('Demanding', 'Aluguel maior que 50')
cautious_player = Player('Cautious', 'Só compra se sobrar 80 de saldo')
random_player = Player('Random', 'Probabilidade de 50%')

all_players = [impulsive_player, demanding_player,
               cautious_player, random_player]

all_balance = []
for player in all_players:
    all_balance.append(player.balance)

print(max(all_balance))

if max(all_balance) < 0:
    game = False

print('game')

lista_teste = [1, 3, 3, 2]

for value in lista_teste:
    print(lista_teste.count(value))

lista_teste = []

print(len(lista_teste))

teste = [player for player in all_players]

print(teste)


print([x for x in range(1, 7)])

print(randint(0, 1))

print(impulsive_player.is_alive())

# with open('./banco_imobiliario/teste.csv', 'w+', newline='') as arquivo:
#     escritor_csv = writer(arquivo)
#     filme = None
#     escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
#     while filme != 'sair':
#         filme = input("Titulo: ")
#         if filme != 'sair':

#             genero = input("Genrero: ")
#             duracao = input("Duracao: ")
#             escritor_csv.writerow([filme, genero, duracao])

play = input('Deseja jogar? [s/n]').lower()
print(play)
