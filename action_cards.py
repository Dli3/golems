'''
These are the action cards which allows you to alter your
crystal cart by upgrading, trading, or gaining crystals.

There's a total of 53 action cards.

Each player starts with a plus2yellow and upgrade_2 action card.
These two cards will be included in the player class.
'''


def upgrade(player):
    if player.yellow or player.green or player.blue or player.pink > 0:

        print(f"{player.name}'s hand: {player.yellow} yellow, {player.green} green, {player.blue} blue, and {player.pink} pink.")
        acceptable = ['pass']
        while True:
            try:
                print('Upgrade options:')
                print('"pass" to skip upgrade.')
                if player.yellow > 0:
                    acceptable.append('yellow')
                    acceptable.append('y')
                    print('Yellow or y')
                if player.green > 0:
                    acceptable.append('green')
                    acceptable.append('g')
                    print('Green or g')
                if player.blue > 0:
                    acceptable.append('blue')
                    acceptable.append('b')
                    print('Blue or b')

                try:
                    upgrade = input().lower()
                    while upgrade not in acceptable:
                        upgrade = input(
                            'ERROR: Please enter a valid crystal option.\n').lower()
                        continue

                    if upgrade in acceptable:
                        if player.yellow > 0:
                            if upgrade == 'yellow' or upgrade == 'y':
                                player.yellow += -1
                                player.green += 1
                                assert player.yellow > -1

                        if player.green > 0:
                            if upgrade == 'green' or upgrade == 'g':
                                player.green += -1
                                player.blue += 1
                                assert player.green > -1

                        if player.blue > 0:
                            if upgrade == 'blue' or upgrade == 'b':
                                player.blue += -1
                                player.pink += 1
                                assert player.blue > -1
                        if upgrade == 'pass':
                            print('Player decided not to upgrade.')
                            break
                except:
                    print(
                        'ERROR: Invalid input.\nPlease enter a valid input.')
                    continue
                break
            except Exception as e:
                print(str(e))
                return False
    else:
        print('ERROR: Insufficient funds.')
        return False
    return player


def upgrade_2(player):
    if player.yellow or player.green or player.blue or player.pink > 0:
        print('CRYSTAL UPGRADES: 2')
        print('Please select a crystal to upgrade.')
        upgrade(player)
        print('CRYSTAL UPGRADES: 1')
        print('Please select a second crystal to upgrade.')
        upgrade(player)
    else:
        print('ERROR: No crystals to upgrade.')
    return player


def upgrade_3(player):
    if player.yellow or player.green or player.blue or player.pink > 0:
        print('CRYSTAL UPGRADES: 3')
        print('Please select a crystal to upgrade.')
        upgrade(player)
        print('CRYSTAL UPGRADES: 2')
        print('Please select a second crystal to upgrade.')
        upgrade(player)
        print('CRYSTAL UPGRADES: 1')
        print('Please select a third crystal to upgrade.')
        upgrade(player)
    else:
        print('ERROR: No crystals to upgrade.')
    return player


#! The actions dictionary has the keys that will be in a list.
# The user will use an action card that references this list.
# The action card will then take the numbers in the list with the index of
# yellow, green, blue, and pink.
actions_dict = {
    'upgrade2': upgrade_2,
    'plus2yellow': [2, 0, 0, 0],
    'minus2yellow_plus2green': [-2, 2, 0, 0],
    'minus2yellow_plus1blue': [-2, 0, 1, 0],
    'minus3yellow_plus1pink': [-3, 0, 0, 1],
    'minus3yellow_plus1green1blue': [-3, 1, 1, 0],
    'minus4yellow_plus1blue1pink': [-4, 0, 1, 1],
    'minus5yellow_plus2pink': [-5, 0, 0, 2],
    'minus5yellow_plus3blue': [-5, 0, 3, 0],
    'minus4yellow_plus2blue': [-4,  0, 2, 0],
    'minus3yellow_plus3green': [-3, 3, 0, 0],
    'minus1green_plus3yellow': [3, -1, 0, 0],
    'minus2green_plus2blue': [0, -2, 2, 0],
    'minus2green_plus1pink2yellow': [2, -2, 0, 1],
    'minus2green_plus1blue3yellow': [3, -2, 1, 0],
    'minus3green_plus1pink1blue1yellow': [1, -3, 1, 1],
    'minus3green_plus2blue2yellow': [2, -3, 2, 0],
    'minus3green_plus2pink': [0, -3, 0, 2],
    'minus3green_plus3blue': [0, -3, 3, 0],
    'minus1green1yellow_plus1pink': [-1, -1, 0, 1],
    'minus1blue_plus2green': [0, 2, -1, 0],
    'minus1blue_plus1green4yellow': [4, 1, -1, 0],
    'minus1blue_plus2green1yellow': [1, 2, -1, 0],
    'minus2blue_plus2pink': [0, 0, -2, -2],
    'minus2blue_plus1pink2green': [0, 2, -2, 1],
    'minus2blue_plus3green2yellow': [2, 3, -2, 0],
    'minus2blue_plus1pink1green2yellow': [2, 1, -2, 1],
    'minus3blue_plus3pink': [0, 0, -3, -3],
    'minus1blue2yellow_plus2pink': [-2, 0, -1, 2],
    'minus1pink_plus2blue': [0, 0, 2, -1],
    'minus1pink_plus3green': [0, 3, 0, -1],
    'minus1pink_plus1blue1green1yellow': [1, 1, 1, -1],
    'minus1pink_plus2green2yellow': [2, 2, 0, -1],
    'minus1pink_plus1blue3yellow': [3, 0, 1, -1],
    'minus2pink_plus3blue1green1yellow': [1, 1, 3, -2],
    'minus2pink_plus2blue3green': [0, 3, 2, -2],
    'plus3yellow': [3, 0, 0, 0],
    'plus4yellow': [4, 0, 0, 0],
    'plus1green1yellow': [1, 1, 0, 0],
    'plus2green': [0, 2, 0, 0],
    'plus1blue': [0, 0, 1, 0],
    'plus1blue1yellow': [1, 0, 1, 0],
    'plus1pink': [0, 0, 0, 1],
    'plus1green2yellow': [2, 1, 0, 0],
    'upgrade3': upgrade_3
}
