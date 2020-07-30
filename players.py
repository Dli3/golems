from golems import golems_cards
import random
from action_cards import plus_two_yellow, upgrade_two, minus2yellow_plus2green


class Player():
    def __init__(self, points, score):
        self.points = points
        self.score = score
        self.crystal_cart = {'max': 10,
                             'yellow': 0,
                             'green': 0,
                             'blue': 0,
                             'pink': 0}
        self.golems = 0
        self.hand = []
        self.discard_pile = []


player = Player(0, 0)
player.points += 1
player.score += 1
print(player.points)

print(player.score)

print(player.crystal_cart['max'])
print(player.crystal_cart['yellow']+5)


d = random.choice(list(golems_cards.keys()))
print(d)

print(golems_cards[d]['requirements'])
a = golems_cards[d]['requirements']
print(a.values())

# print(a['yellow'])
# player.crystal_cart['yellow'] -= a['yellow']

print(player.crystal_cart)

# print(actions)

# f = actions['card_1']['action'](player.crystal_cart)
# print(f)

# player.hand.append(plus_two_yellow)
# player.hand.append(upgrade_two)


card_list = [plus_two_yellow,
             upgrade_two, minus2yellow_plus2green]
for card in card_list:
    print(card)
    player.hand.append(card)
    print(player.hand)
player.hand[2](player.crystal_cart)
print(player.crystal_cart)
