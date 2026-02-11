from csv import writer

from pandas import read_csv

from player import game_still_on, player_play
from puzzle import create_players, create_puzzle

game_number = 0

print('Jogos iniciados')

with open('./banco_imobiliario/game_status.csv', 'w+', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    escritor_csv.writerow(
        ['Partida Numero', 'Nome Vencedor', 'Estrategia Vencedor',
         'Numero de turnos', 'Numero vezes voltou inicio', 'Como finalizou'])

    while game_number < 300:
        all_players = []
        puzzle = []
        game = True
        turn = 1

        all_players = create_players()

        puzzle = create_puzzle(all_players)

        while game and turn < 1001:

            for player in all_players:

                if player.is_alive():

                    puzzle = player_play(puzzle, player)

            game_status = game_still_on(all_players, turn, game)

            game = game_status['game']

            if game:
                turn += 1

            else:
                escritor_csv.writerow([game_number + 1,
                                       game_status['winner_name'],
                                       game_status['winner_strategy'],
                                       game_status['turn'],
                                       game_status['winner_complete_puzzle'],
                                       game_status['how_it_end']])
                game_number += 1

print('Jogos finalizados')

game_status_df = read_csv('./banco_imobiliario/game_status.csv')

game_status_timeout = \
    game_status_df[game_status_df['Como finalizou'] == 'timeout']

print(f"Quantidade de jogos com timeout: {game_status_timeout.shape[0]}")

game_status_turn = game_status_df['Numero de turnos'].mean(axis=0)

print(f"Média de turnos por partida, contando timeout: \
    {round(game_status_turn)}")

game_status_turn_no_timeout = \
    game_status_df[game_status_df['Como finalizou']
                   != 'timeout']['Numero de turnos'].mean(axis=0)

print(f"Média de turnos por partida, sem timeout: \
    {round(game_status_turn_no_timeout)}")

winner_strategy = ['Impulsive', 'Random', 'Demanding', 'Cautious']

total = game_status_df['Estrategia Vencedor'].count()

highest_percentual = 0
highest_strategy_wr = ''

for strategy in winner_strategy:
    strategy_count = game_status_df.loc[strategy].count()
    percentual_strategy = round((strategy_count / total) * 100, 2)
    if percentual_strategy > highest_percentual:
        highest_percentual = percentual_strategy
        highest_strategy_wr = strategy
    print(f"A estratégia '{strategy}'' tem uma porcentagem de vitória de: \
        {round(percentual_strategy, 2)}% \n")

print(f"A maior taxa de vitória é: {highest_percentual} % estratégia\
    '{highest_strategy_wr}'")
