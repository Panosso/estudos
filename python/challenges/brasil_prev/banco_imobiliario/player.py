from random import randint

from dice import dice_face


class Player:
    def __init__(self, name, buy_rule) -> None:
        self.name = name
        self.buy_rule = buy_rule
        self.balance = 300
        self.dice_value = 0
        self.player_alive = True
        self.puzzle_position = 0
        self.complete_puzzle = 0

    def is_alive(self):
        return self.player_alive

    def player_status(self):
        status = f'''
                     Nome: {self.name}, 
                     regra de compra: {self.buy_rule},
                     ultimo valor no dado: {self.dice_value}, 
                     Está no jogo: {self.is_alive()},
                     está na posição: {self.puzzle_position}
                    '''
        return status


def buy_slot(value, player):
    player.balance -= value


def pay_rent(value, player_pay, player_receive):

    if 'game' not in (player_pay, player_receive):
        old_balance = player_pay.balance
        current_balance = player_pay.balance - value
        player_pay.balance = current_balance

        if current_balance < 0:
            player_pay.player_alive = False
            player_receive.balance += old_balance

        else:
            player_receive.balance += value


def player_play(puzzle: list, player: Player):

    moviment = dice_face()
    current_position = player.puzzle_position
    new_position = moviment + current_position
    puzzle_location = puzzle[current_position]

    if new_position > 20:
        player.balance += 100
        new_position = new_position - 21
        player.complete_puzzle += 1

    puzzle_location['player_in'].pop(
        puzzle_location['player_in'].index(player))

    if puzzle_location['owner'] == '' and \
            (player.balance + puzzle_location['slot_price']) > 0:

        if player.buy_rule == 'Impulsive':
            puzzle_location['owner'] = player
            buy_slot(puzzle_location['slot_price'], player)

        elif player.buy_rule == 'Demanding':
            if puzzle_location['rent'] > 50:
                puzzle_location['owner'] = player
                buy_slot(puzzle_location['slot_price'], player)

        elif player.buy_rule == 'Cautious':
            if puzzle_location['slot_price'] - player.balance > 80:
                puzzle_location['owner'] = player
                buy_slot(puzzle_location['slot_price'], player)

        elif player.buy_rule == 'Random':
            if randint(0, 1) == 1:
                puzzle_location['owner'] = player
                buy_slot(puzzle_location['slot_price'], player)

    elif puzzle_location['owner'] != '':

        pay_rent(puzzle_location['rent'],
                 player,
                 puzzle_location['owner'])

        if not player.is_alive():
            for location in puzzle:
                if location['owner'] == player:
                    location['owner'] = ''

    player.puzzle_position = new_position
    puzzle[new_position]['player_in'].append(player)

    return puzzle


def game_still_on(all_players: list, turn: int, game: bool):

    game_status = {'winner_name': '', 'winner_strategy': '',
                   'turn': 0, 'winner_complete_puzzle': 0,
                   'how_it_end': '', 'game': True}

    players_alive = []
    players_balance = []
    winners = []
    winner_name = ''
    winner_srategy = ''
    higher_balance = 0
    player_name = ''
    player_strategy = ''
    player_complete_puzzle = 0

    for player in all_players:
        if player.is_alive():
            players_alive.append(player)
            player_name = player.name
            player_strategy = player.buy_rule
            player_complete_puzzle = player.complete_puzzle

    if len(players_alive) == 1:
        # print(
        #     f'Jogador(a) {player_name} foi o '
        #     f'vitorioso usando a estratégia {player_strategy}')

        game_status['winner_name'] = player_name
        game_status['winner_strategy'] = player_strategy
        game_status['turn'] = turn
        game_status['winner_complete_puzzle'] = player_complete_puzzle
        game_status['how_it_end'] = 'saldo_positivo'
        game_status['game'] = False

    elif turn == 1000:

        for player in players_alive:

            players_balance.append({'name': player.name,
                                    'balance': player.balance,
                                    'strategy': player.buy_rule})

            players_balance = sorted(
                players_balance, key=(lambda v: v['balance']), reverse=True)

            higher_balance = players_balance[0]['balance']

        winners = list(
            filter(lambda w: w['balance'] == higher_balance, players_balance))

        if len(winners) == 1:
            winner_name = winners[0]['name']
            winner_srategy = winners[0]['strategy']
            # print(
            #     f'Jogador(a) {winner_name} foi o vencedor por saldo positivo'
            #     f' usando a estratégia {winner_srategy}')

        else:
            for winner in winners:
                winner_name += winner['name'] + ' '
                winner_srategy += winner['strategy'] + ' '

            # print(
            #     f'Jogadores vencedores são: {winner_name}utilizando a'
            #     f' estratégia {winner_srategy}respectivamente')

        game_status['winner_name'] = player_name
        game_status['winner_strategy'] = player_strategy
        game_status['turn'] = turn
        game_status['winner_complete_puzzle'] = player_complete_puzzle
        game_status['how_it_end'] = 'timeout'
        game_status['game'] = False

    return game_status
