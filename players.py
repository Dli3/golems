from golems import golems_cards
import random
from action_cards import plus2yellow, upgrade_2


class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.golems = 0
        self.crystal_cart = {'max': 10,
                             'yellow': 0,
                             'green': 0,
                             'blue': 0,
                             'pink': 0}

        self.hand = [plus2yellow, upgrade_2]
        self.discard_pile = []


# player = Player(0, 0)
# player.points += 1
# player.score += 1
# print(player.points)

# print(player.score)

# print(player.crystal_cart['max'])
# print(player.crystal_cart['yellow']+5)


# d = random.choice(list(golems_cards.keys()))
# print(d)

# print(golems_cards[d]['requirements'])
# a = golems_cards[d]['requirements']
# print(a.values())

# # print(a['yellow'])
# # player.crystal_cart['yellow'] -= a['yellow']

# print(player.crystal_cart)

# # print(actions)

# # f = actions['card_1']['action'](player.crystal_cart)
# # print(f)
