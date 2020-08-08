from action_cards import*
from players import Player
from golems import golems_cards
import random
from check_board import*


# The actions and golems list.
action_cards_list = [card for card in actions_dict]
golems_list = [golem for golem in golems_cards]

# Creating golem board which contains 5 golems at a time(or until deckout).
golems_board = create_golems_board(golems_list)
# print(golems_board)

# Creating action cards board which contains 6 action cards at at time(or until deckout).


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
