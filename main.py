from action_cards import*
from players import Player
from golems import golems_cards
import random
from check_board import*
from board import Board

p = ['dennis', 'test']
board = Board(players_list=p)
board.check_golem_board()
a = board.golems_board[1]
board.board_state()
print(board.players_list)
del board.golems_board[1]
board.check_golem_board()
board.board_state()


# #! Creating the players playing the game.
# num_players = define_number_of_players()
# players_list = []
# for total_players in range(num_players):
#     name = input(f'\nWhat is your name player {total_players + 1}?\n')
#     players_list.append(Player(name))


# #! Game play
# last_round_players = []

# while check_max_golems(players_list) != 5:
#     for player in players_list:
#         if check_max_golems(players_list) != 5:
#             player.golems += 1
#             print(player.name)
#             print(player.golems)

# else:
#     for player in players_list:
#         if player.golems != 5:
#             last_round_players.append(player)

# for player in last_round_players:
#     print(player.name)
