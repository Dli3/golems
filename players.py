from golems import golems_cards
import random
from action_cards import plus2yellow, upgrade_2


class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.golems = 0
        self.crystal_capacity = 0
        self.yellow = 0
        self.green = 0
        self.blue = 0
        self.pink = 0
        self.hand = [plus2yellow, upgrade_2]
        self.discard_pile = []

    def update_yellow(self, yellow):
        self.yellow += yellow

    def update_green(self, green):
        self.green += green

    def update_blue(self, blue):
        self.blue += blue

    def update_pink(self, pink):
        self.pink += pink

    def update_golems(self):
        self.golems += 1

    def update_points(self, points):
        self.points += points

    def update_hand(self, card):
        self.hand.append(card)

    def update_crystal_capacity(self, crystals):
        self.crystal_capacity += crystals

    def check_crystal_crystal_capacity(self):
        while self.crystal_capacity > 10:
            try:
                print(
                    f"\n{self.name}'s crystal cart is over crystal_capacity by {self.crystal_capacity-10}")
                print(
                    f'Available crystals to discard:\nYellow: {self.yellow}\nGreen: {self.green}\nBlue: {self.blue}\nPink: {self.pink}')
                discard_crystal = input(
                    'Which crystal would you like to discard?\nOptions:\nyellow or y\ngreen or g\nblue or b\npink or p\n').lower()
                if discard_crystal == 'yellow' or discard_crystal == 'y':
                    if self.yellow > 0:
                        self.yellow -= 1
                        self.crystal_capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'green' or discard_crystal == 'g':
                    if self.green > 0:
                        self.green -= 1
                        self.crystal_capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'blue' or discard_crystal == 'b':
                    if self.blue > 0:
                        self.blue -= 1
                        self.crystal_capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                elif discard_crystal == 'pink' or discard_crystal == 'p':
                    if self.pink > 0:
                        self.pink -= 1
                        self.crystal_capacity -= 1
                    else:
                        print('ERROR: Insufficient crystal funds!')
                else:
                    print(
                        'ERROR: Invalid input. Please enter the following valid options:\nyellow or y\ngreen or g\nblue or b\npink or p')
            except:
                break

    def crystal_sum(self):
        crystal_sum = self.yellow + self.green + self.blue + self.pink
        return crystal_sum

    def pay_in_crystals(self):
        crystal_sum = self.crystal_sum()
        if crystal_sum > 0:
            while True:
                print(f"Which crystal would you like to pay in?\nOptions:")
                if self.yellow > 0:
                    print(f'{self.yellow} yellow crystals')
                if self.green > 0:
                    print(f'{self.green} green crystals')
                if self.blue > 0:
                    print(f'{self.blue} blue crystals')
                if self.pink > 0:
                    print(f'{self.pink} pink crystals')

                acceptable = ['yellow', 'y', 'green',
                              'g', 'blue', 'b', 'pink', 'p']
                try:
                    payment = input().lower()
                    assert payment in acceptable
                    if payment == 'yellow' or payment == 'y':
                        if self.yellow > 0:
                            self.yellow -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'green' or payment == 'g':
                        if self.green > 0:
                            self.green -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'blue' or payment == 'b':
                        if self.blue > 0:
                            self.blue -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'pink' or payment == 'p':
                        if self.pink > 0:
                            self.pink -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                except ValueError:
                    print('ERROR: Please enter a valid input.')
                break
        return self
