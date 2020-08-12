'''
These are the action cards which allows you to alter your
crystal cart by upgrading, trading, or gaining crystals.

There's a total of 53 action cards.

Each player starts with a plus2yellow and upgrade_2 action card.
These two cards will be included in the player class.
'''


def upgrade(player):
    upgrade = input(
        'Options:\nyellow or y\ngreen or g\nblue or b\n').lower()
    if upgrade == 'yellow' or upgrade == 'y':
        player.yellow += 1
    elif upgrade == 'green' or upgrade == 'g':
        player.green += 1
    elif upgrade == 'blue' or upgrade == 'b':
        player.blue += 1
    return player


def plus2yellow(player):
    print('Plus 2 yellow')
    player.yellow += 2
    player.crystal_capacity += 2
    return player


def upgrade_2(player):
    print('Select first crystal to upgrade.')
    upgrade(player)
    print("Select second crystal to upgrade.")
    upgrade(player)
    return player


def minus2yellow_plus2green(player):
    print('Trade 2 yellows for 2 greens.')
    player.yellow += -2
    player.green += 2
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 0
    return player


def minus2yellow_plus1blue(player):
    print('Trade 2 yellows for 1 blue.')
    player.yellow += -2
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.crystal_capacity += -1
    return player


def minus3yellow_plus1pink(player):
    print('Trade 3 yellows for 1 pink.')
    player.yellow += -3
    player.green += 0
    player.blue += 0
    player.pink += 1
    player.crystal_capacity += -2
    return player


def minus3yellow_plus1green1blue(player):
    print('Trade 3 yellow for 1 green and 1 blue.')
    player.yellow += -3
    player.green += 1
    player.blue += 1
    player.pink += 0
    player.crystal_capacity += -1
    return player


def minus4yellow_plus1blue1pink(player):
    print('Trade 4 yellow for 1 blue and 1 pink.')
    player.yellow += -4
    player.green += 0
    player.blue += 1
    player.pink += 1
    player.crystal_capacity += -2
    return player


def minus5yellow_plus2pink(player):
    print('Trade 5 yellow for 2 pink.')
    player.yellow += -5
    player.green += 0
    player.blue += 0
    player.pink += 2
    player.crystal_capacity += -3
    return player


def minus5yellow_plus3blue(player):
    print('Trade 5 yellow for 3 blue.')
    player.yellow += -5
    player.green += 0
    player.blue += 3
    player.pink += 0
    player.crystal_capacity += -2
    return player


def minus4yellow_plus2blue(player):
    print('Trade 4 yellow for 2 blue.')
    player.yellow += -4
    player.green += 0
    player.blue += 2
    player.pink += 0
    player.crystal_capacity += -2
    return player


def minus3yellow_plus3green(player):
    print('Trade 3 yellow for 3 green.')
    player.yellow += -3
    player.green += 3
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 0
    return player


def minus1green_plus3yellow(player):
    print('Trade 1 green for 3 yellow.')
    player.yellow += 3
    player.green += -1
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 2
    return player


def minus2green_plus2blue(player):
    print('Trade 2 green for 2 blue.')
    player.yellow += 0
    player.green += -2
    player.blue += 2
    player.pink += 0
    player.crystal_capacity += 0
    return player


def minus2green_plus1pink2yellow(player):
    print('Trade 2 green for 1 pink and 2 yellow.')
    player.yellow += 2
    player.green += -2
    player.blue += 0
    player.pink += 1
    player.crystal_capacity += 1
    return player


def minus2green_plus1blue3yellow(player):
    print('Trade 2 green for 1 blue 3 yellow.')
    player.yellow += 3
    player.green += -2
    player.blue += 1
    player.pink += 0
    player.crystal_capacity += 2
    return player


def minus3green_plus1pink1blue1yellow(player):
    print('Trade 3 green for 1 pink 1 blue and 1 yellow.')
    player.yellow += 1
    player.green += -3
    player.blue += 1
    player.pink += 1
    player.crystal_capacity += 0
    return player


def minus3green_plus2blue2yellow(player):
    print('Trade 3 green for 2 blue and 2 yellow.')
    player.yellow += 2
    player.green += -3
    player.blue += 2
    player.pink += 0
    player.crystal_capacity += 1
    return player


def minus3green_plus2pink(player):
    print('Trade 3 green for 2 pink.')
    player.yellow += 0
    player.green += -3
    player.blue += 0
    player.pink += 2
    player.crystal_capacity += -1
    return player


def minus3green_plus3blue(player):
    print('Trade 3 green for 3 blue.')
    player.yellow += 0
    player.green += -3
    player.blue += 3
    player.pink += 0
    player.crystal_capacity += 0
    return player


def minus1green1yellow_plus1pink(player):
    print('Trade 1 green and 1 yellow for 1 pink')
    player.yellow += -1
    player.green += -1
    player.blue += 0
    player.pink += 1
    player.crystal_capacity += -1
    return player


def minus1blue_plus2green(player):
    print('Trade 1 blue for 2 greens.')
    player.yellow += 0
    player.green += 2
    player.blue += -1
    player.pink += 0
    player.crystal_capacity += 1
    return player


def minus1blue_plus1green4yellow(player):
    print('Trade 1 blue for 1 green and 4 yellows.')
    player.yellow += 4
    player.green += 1
    player.blue += -1
    player.pink += 0
    player.crystal_capacity += 4
    return player


def minus1blue_plus2green1yellow(player):
    print('Trade 1 blue for 2 green and 1 yellow.')
    player.yellow += 1
    player.green += 2
    player.blue += -1
    player.pink += 0
    player.crystal_capacity += 2
    return player


def minus2blue_plus2pink(player):
    print('Trade 2 blue for 2 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += -2
    player.pink += 2
    player.crystal_capacity += 0
    return player


def minus2blue_plus1pink2green(player):
    print('Trade 2 blue for 1 pink and 2 green.')
    player.yellow += 0
    player.green += 2
    player.blue += -2
    player.pink += 1
    player.crystal_capacity += 1
    return player


def minus2blue_plus3green2yellow(player):
    print('Trade 2 blue for 3 green and 2 yellow.')
    player.yellow += 2
    player.green += 3
    player.blue += -2
    player.pink += 0
    player.crystal_capacity += 3
    return player


def minus2blue_plus1pink1green2yellow(player):
    print('Trade 2 blue for 1 pink, 1 green, and 2 yellow.')
    player.yellow += 2
    player.green += 1
    player.blue += -2
    player.pink += 1
    player.crystal_capacity += 2
    return player


def minus3blue_plus3pink(player):
    print('Trade 3 blue for 3 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += -3
    player.pink += 3
    player.crystal_capacity += 0
    return player


def minus1blue2yellow_plus2pink(player):
    print('Trade 1 blue and 2 yellow for 2 pink.')
    player.yellow += -2
    player.green += 0
    player.blue += -1
    player.pink += 2
    player.crystal_capacity += -1
    return player


def minus1pink_plus2blue(player):
    print('Trade 1 pink for 2 blue.')
    player.yellow += 0
    player.green += 0
    player.blue += 2
    player.pink += -1
    player.crystal_capacity += 1
    return player


def minus1pink_plus3green(player):
    print('Trade 1 pink for 3 green.')
    player.yellow += 0
    player.green += 3
    player.blue += 0
    player.pink += -1
    player.crystal_capacity += 2
    return player


def minus1pink_plus1blue1green1yellow(player):
    print('Trade 1 pink for 1 blue 1 green 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 1
    player.pink += -1
    player.crystal_capacity += 2
    return player


def minus1pink_plus2green2yellow(player):
    print('Trade 1 pink for 2 green 1 yellow.')
    player.yellow += 2
    player.green += 2
    player.blue += 0
    player.pink += -1
    player.crystal_capacity += 3
    return player


def minus1pink_plus1blue3yellow(player):
    print('Trade 1 pink for 1 blue and 3 yellow.')
    player.yellow += 3
    player.green += 0
    player.blue += 1
    player.pink += -1
    player.crystal_capacity += 3
    return player


def minus2pink_plus3blue1green1yellow(player):
    print('Trade 2 pink for 3 blue, 1 green, and 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 3
    player.pink += -2
    player.crystal_capacity += 3
    return player


def minus2pink_plus2blue3green(player):
    print('Trade 2 pink for 2 blue and 3 green.')
    player.yellow += 0
    player.green += 3
    player.blue += 2
    player.pink += -2
    player.crystal_capacity += 3
    return player


def plus3yellow(player):
    print('Gain 3 yellow.')
    player.yellow += 3
    player.green += 0
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 3
    return player


def plus4yellow(player):
    print('Gain 4 yellow.')
    player.yellow += 4
    player.green += 0
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 4
    return player


def plus1green1yellow(player):
    print('Gain 1 green and 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 2
    return player


def plus2green(player):
    print('Gain 2 green.')
    player.yellow += 0
    player.green += 2
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 2
    return player


def plus1blue(player):
    print('Gain 1 blue.')
    player.yellow += 0
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.crystal_capacity += 1
    return player


def plus1blue1yellow(player):
    print('Gain 1 blue and 1 yellow.')
    player.yellow += 1
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.crystal_capacity += 2
    return player


def plus1pink(player):
    print('Gain 1 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += 0
    player.pink += 1
    player.crystal_capacity += 1
    return player


def plus1green2yellow(player):
    print('Gain 1 green and 2 yellow.')
    player.yellow += 2
    player.green += 1
    player.blue += 0
    player.pink += 0
    player.crystal_capacity += 3
    return player


def upgrade3(player):
    print('Three crystal upgrades.')
    print('Select first crystal to upgrade.')
    upgrade(player)
    print("Select second crystal to upgrade.")
    upgrade(player)
    print("Select third crystal to upgrade.")
    upgrade(player)
    return player


actions_dict = {
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
    'upgrade3': upgrade3
}
