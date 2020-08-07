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


#! Creating the players playing the game.

num_players = define_number_of_players()

assert num_players < 6

players_list = []

for total_players in range(num_players):
    name = input(f'What is your name player {total_players + 1}?\n')
    players_list.append(Player(name))

print(players_list)
print(players_list[1].name)

print(players_list[1].crystal_cart)
