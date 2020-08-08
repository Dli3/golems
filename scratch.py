from action_cards import*
from players import Player
from golems import golems_cards
import random
from check_board import*
cart = Player('Dennis')
cart.yellow += 10
cart.green += 10
cart.blue += 10
cart.pink += 10
hand = []
print(cart.yellow)
print(cart.green)
print(cart.blue)
print(cart.pink)
print(cart.capacity)
d = random.choice(action_cards_list)
hand.append(d)

print(d)
print(hand)
actions_dict[hand[0]](cart)
print(cart.yellow)
print(cart.green)
print(cart.blue)
print(cart.pink)
print(cart.capacity)
# action_cards_list
