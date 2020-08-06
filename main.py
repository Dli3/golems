from action_cards import*
from players import Player
from golems import golems_cards
import random
from check_board import*

actions_dict = {
    'minus2yellow_plus2green': minus2yellow_plus2green,
    'minus2yellow_plus1blue': minus2yellow_plus1blue,
    'minus3yellow_plus1pink': minus3yellow_plus1pink,
    'minus3yellow_plus1green1blue': minus3yellow_plus1green1blue,
    'minus4yellow_plus1blue1pink': minus4yellow_plus1blue1pink,
    'minus5yellow_plus2pink': minus5yellow_plus2pink,
    'minus5yellow_plus3blue': minus5yellow_plus3blue,
    'minus4yellow_plus2blue': minus4yellow_plus2blue,
    'minus3yellow_plus3green': minus3yellow_plus3green,
    'minus1green_plus3yellow': minus1green_plus3yellow,
    'minus2green_plus2blue': minus2green_plus2blue,
    'minus2green_plus1pink2yellow': minus2green_plus1pink2yellow,
    'minus2green_plus1blue3yellow': minus2green_plus1blue3yellow,
    'minus3green_plus1pink1blue1yellow': minus3green_plus1pink1blue1yellow,
    'minus3green_plus2blue2yellow': minus3green_plus2blue2yellow,
    'minus3green_plus2pink': minus3green_plus2pink,
    'minus3green_plus3blue': minus3green_plus3blue,
    'minus1green1yellow_plus1pink': minus1green1yellow_plus1pink,
    'minus1blue_plus2green': minus1blue_plus2green,
    'minus1blue_plus1green4yellow': minus1blue_plus1green4yellow,
    'minus1blue_plus2green1yellow': minus1blue_plus2green1yellow,
    'minus2blue_plus2pink': minus2blue_plus2pink,
    'minus2blue_plus1pink2green': minus2blue_plus1pink2green,
    'minus2blue_plus3green2yellow': minus2blue_plus3green2yellow,
    'minus2blue_plus1pink1green2yellow': minus2blue_plus1pink1green2yellow,
    'minus3blue_plus3pink': minus3blue_plus3pink,
    'minus1blue2yellow_plus2pink': minus1blue2yellow_plus2pink,
    'minus1pink_plus2blue': minus1pink_plus2blue,
    'minus1pink_plus3green': minus1pink_plus3green,
    'minus1pink_plus1blue1green1yellow': minus1pink_plus1blue1green1yellow,
    'minus1pink_plus2green2yellow': minus1pink_plus2green2yellow,
    'minus1pink_plus1blue3yellow': minus1pink_plus1blue3yellow,
    'minus2pink_plus3blue1green1yellow': minus2pink_plus3blue1green1yellow,
    'minus2pink_plus2blue3green': minus2pink_plus2blue3green,
    'plus3yellow': plus3yellow,
    'plus4yellow': plus4yellow,
    'plus1green1yellow': plus1green1yellow,
    'plus2green': plus2green,
    'plus1blue': plus1blue,
    'plus1blue1yellow': plus1blue1yellow,
    'plus1pink': plus1pink,
    'plus1green2yellow': plus1green2yellow,
    'upgrade3': upgrade3,
}

# The actions and golems deck.
action_cards_list = [card for card in actions_dict]
golems_list = [golem for golem in golems_cards]

# The 5 randomly selected golems.
golems_board = create_golems_board(golems_list)


print(golems_board)
a = golems_board[1]

player = Player('Dennis')
player.crystal_cart['yellow'] += 10
player.crystal_cart['green'] += 10
player.crystal_cart['blue'] += 10
player.crystal_cart['pink'] += 10

capture_golem(player, 3, golems_board, player.crystal_cart, golems_cards)


# #! Creating the players playing the game.
# num_players = int(input('How many players?\n'))
# assert num_players < 6

# total_players = 0
# player_names = []


# if total_players in range(num_players):
#     player1 = input(f'What is your name player {total_players + 1}?\n')
#     player_1 = Player(player1)
#     total_players += 1
#     player_names.append(player_1.name)
# else:
#     player_1 = None

# if total_players in range(num_players):
#     player2 = input(f'What is your name player {total_players + 1}?\n')
#     player_2 = Player(player2)
#     total_players += 1
#     player_names.append(player_2.name)
# else:
#     player_2 = None

# if total_players in range(num_players):
#     player3 = input(f'What is your name player {total_players + 1}?\n')
#     player_3 = Player(player3)
#     total_players += 1
#     player_names.append(player_3.name)
# else:
#     player_3 = None

# if total_players in range(num_players):
#     player4 = input(f'What is your name player {total_players + 1}?\n')
#     player_4 = Player(player4)
#     total_players += 1
#     player_names.append(player_4.name)
# else:
#     player_4 = None

# if total_players in range(num_players):
#     player5 = input(f'What is your name player {total_players + 1}?\n')
#     player_5 = Player(player5)
#     total_players += 1
#     player_names.append(player_5.name)
# else:
#     player_5 = None

# print(f'Total players: {total_players}')
# print(f'Players: {player_names}')


# #! Actual players dictionary.
# players = {}
# if player_1 != None:
#     players['player_1'] = player_1
# if player_2 != None:
#     players['player_2'] = player_2
# if player_3 != None:
#     players['player_3'] = player_3
# if player_4 != None:
#     players['player_4'] = player_4
# if player_5 != None:
#     players['player_5'] = player_5

# #! Checking if any of the players have 5 golems.
# while players['player_1'].golems < 5 and players['player_2'].golems < 5:
#     for player in players:
#         print(players[player].crystal_cart)
#         print(players[player].name)
