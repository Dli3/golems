from .golems import golems_cards
import random


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
        self.hand = ['upgrade2', 'plus2yellow']
        self.discard_pile = []

    def update_yellow(self, yellow):
        self.yellow += yellow
        self.crystal_capacity += yellow
        return self.yellow

    def update_green(self, green):
        self.green += green
        self.crystal_capacity += green
        return self.green

    def update_blue(self, blue):
        self.blue += blue
        self.crystal_capacity += blue
        return self.blue

    def update_pink(self, pink):
        self.pink += pink
        self.crystal_capacity += pink
        return self.pink

    def update_golems(self):
        self.golems += 1
        return self.golems

    def update_points(self, points):
        self.points += points
        return self.points

    def update_hand(self, card):
        self.hand.append(card)
        return self.hand

    def update_crystal_capacity(self, crystals):
        self.crystal_capacity += crystals
        return self.crystal_capacity

    def check_crystal_capacity(self):
        while self.crystal_capacity > 10:
            try:
                print(f'{self.name} crystal cart count: {self.crystal_capacity}')
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
                print(
                    f"Player's crystal count is below 10.\n{self.name}'s crystal count: {self.crystal_capacity}'")
                break

    def check_total_crystals(self):
        check_total_crystals = self.yellow + self.green + self.blue + self.pink
        print(f'\n{self.name} crystal count: {check_total_crystals}')
        return check_total_crystals

    def pay_in_crystals(self):
        total_crystals = self.check_total_crystals()
        if total_crystals > 0:
            while True:
                print(f"\nWhich crystal would you like to pay in?\nOptions:")
                if self.yellow > 0:
                    print(f'{self.yellow} yellow (y)')
                if self.green > 0:
                    print(f'{self.green} green (g)')
                if self.blue > 0:
                    print(f'{self.blue} blue (b)')
                if self.pink > 0:
                    print(f'{self.pink} pink (p)')

                acceptable = ['yellow', 'y', 'green',
                              'g', 'blue', 'b', 'pink', 'p']
                payment = input('Payment: ')
                if payment not in acceptable:
                    print("\nERROR: Please enter a valid crystal payment.")
                    if self.yellow > 0:
                        print(f'{self.yellow} yellow (y)')
                    if self.green > 0:
                        print(f'{self.green} green (g)')
                    if self.blue > 0:
                        print(f'{self.blue} blue (b)')
                    if self.pink > 0:
                        print(f'{self.pink} pink (p)')
                    continue
                try:
                    if payment == 'yellow' or payment == 'y':
                        payment = 'yellow'
                        if self.yellow > 0:
                            self.yellow -= 1
                            self.crystal_capacity -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'green' or payment == 'g':
                        payment = 'green'
                        if self.green > 0:
                            self.green -= 1
                            self.crystal_capacity -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'blue' or payment == 'b':
                        payment = 'blue'
                        if self.blue > 0:
                            self.blue -= 1
                            self.crystal_capacity -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                    elif payment == 'pink' or payment == 'p':
                        payment = 'pink'
                        if self.pink > 0:
                            self.pink -= 1
                            self.crystal_capacity -= 1
                        else:
                            print(
                                'ERROR: Insufficient funds. Please select from the available crystal funds.')
                            continue
                except ValueError:
                    print('ERROR: Please enter a valid input.')
                break
        return payment

    def crystal_capacity_counter(self):
        print(f"\n{self.name}'s crystals:")
        print(f"Player's Crystal Capacity: {self.crystal_capacity}")
        print(f"{self.yellow} Yellow crystals")
        print(f"{self.green} Green crystals")
        print(f"{self.blue} Blue crystals")
        print(f"{self.pink} Pink crystals")
        return self.crystal_capacity

    def check_discard_pile(self):
        print(f"\n{self.name}'s discard pile: {self.discard_pile}'")
        return self.discard_pile

    def check_hand(self):
        print(f"\n{self.name}'s hand: {self.hand}'")
        return self.hand

    def check_golems(self):
        print(f"\n{self.name}'s captured golems: {self.golems}'")
        return self.golems

    def crystals_list(self):
        crystals_list = [self.yellow, self.green, self.blue, self.pink]
        return crystals_list

    def check_player_status(self):
        print(f"\n{self.name}'s stats: ")
        print(f"Player's Crystal Capacity: {self.crystal_capacity}")
        print(f"{self.yellow} Yellow crystals")
        print(f"{self.green} Green crystals")
        print(f"{self.blue} Blue crystals")
        print(f"{self.pink} Pink crystals")
        print(f'Golem count: {self.golems}')
        print(f'Points: {self.points}')
        print(f'Hand: {self.hand}')
        print(f'Discard pile: {self.discard_pile}')
