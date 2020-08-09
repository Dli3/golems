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

    def check_crystal_capacity(self):
        while self.capacity > 10:
            try:
                print(
                    f"\n{self.name}'s crystal cart is over capacity by {self.capacity-10}")
                print(
                    f'Available crystals to discard:\nYellow: {self.yellow}\nGreen: {self.green}\nBlue: {self.blue}\nPink: {self.pink}')
                discard_crystal = input(
                    'Which crystal would you like to discard?\nOptions:\nyellow or y\ngreen or g\nblue or b\npink or p\n').lower()
                if discard_crystal == 'yellow' or discard_crystal == 'y':
                    if self.yellow > 0:
                        self.yellow -= 1
                        self.capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'green' or discard_crystal == 'g':
                    if self.green > 0:
                        self.green -= 1
                        self.capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'blue' or discard_crystal == 'b':
                    if self.blue > 0:
                        self.blue -= 1
                        self.capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'pink' or discard_crystal == 'p':
                    if self.pink > 0:
                        self.pink -= 1
                        self.capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                else:
                    print(
                        'ERROR: Invalid input. Please enter the following valid options:\nyellow or y\ngreen or g\nblue or b\npink or p')
            except:
                break
