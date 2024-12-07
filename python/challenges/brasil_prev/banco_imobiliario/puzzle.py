from random import randint

from dice import dice_face
from player import Player


def create_players():

    impulsive_player = Player('Pedro', 'Impulsive')
    demanding_player = Player('Jaque', 'Demanding')
    cautious_player = Player('Yago', 'Cautious')
    random_player = Player('Leonardo', 'Random')

    all_players = [impulsive_player, demanding_player,
                   cautious_player, random_player]

    all_players_order = []
    initial_dices = []

    for player in all_players:

        player.dice_value = dice_face()

        if len(all_players_order) == 0:
            all_players_order.append(player)
            initial_dices.append(player.dice_value)

        else:
            play_again = True

            while play_again:

                if player.dice_value in initial_dices:
                    player.dice_value = dice_face()

                else:
                    all_players_order.append(player)
                    initial_dices.append(player.dice_value)
                    play_again = False

    all_players = sorted(all_players_order, key=(lambda d: d.dice_value))

    return all_players


def create_puzzle(all_players):

    slot_position = 0
    total_quadrant = 300
    percent_value = [0.22, 0.13, 0.40, 0.07, 0.18]
    creating = True

    locations = ['Eiffel Tower', 'Choperia Pinguim', 'museum louvre',
                 'Epcot Center', 'Beto Carreiro World',
                 'Tulemar Bungalows & Villas', 'Hotel Jeri',
                 'Magic Kingdom', 'Animal Kingdom',
                 'Disney Hollywood', 'Vassoura Quebrada',
                 'Taverna Medieval', 'Viking Axes Brasil',
                 'Kongo Pizzaria', 'Jurassic Park Burger', 'Katon',
                 'Fast Escova', 'Areia que canta', 'Pausada', 'Vivenda']

    puzzle = [{'id': slot_position,
               'slot_name': 'start_finish',
               'slot_price': 0,
               'owner': 'game',
               'rent': 0,
               'player_in': [player for player in all_players]}]

    while creating:
        quadrant = 0

        if locations:

            while quadrant < 5:

                slot_position += 1
                location = locations[randint(0, len(locations) - 1)]
                slot_price = round(total_quadrant * percent_value[quadrant])
                slot_rent = round(slot_price * 0.7)

                location_puzzle = {'id': slot_position,
                                   'slot_name': location,
                                   'slot_price': slot_price,
                                   'owner': '',
                                   'rent': slot_rent,
                                   'player_in': []}

                puzzle.append(location_puzzle)

                locations.pop(locations.index(location))
                quadrant += 1

        else:
            creating = False

    return puzzle
