from golems import golems_cards
import random
from action_cards import plus2yellow, upgrade_2


class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.golems = 0
        self.capacity = 10
        self.yellow = 0
        self.green = 0
        self.blue = 0
        self.pink = 0
        self.hand = [plus2yellow, upgrade_2]
        self.discard_pile = []
