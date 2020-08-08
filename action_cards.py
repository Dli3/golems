'''
These are the action cards which allows you to alter your
crystal cart by upgrading, trading, or gaining crystals. 

There's a total of 53 action cards.

Each player starts with a plus2yellow and upgrade_2 action card.
These two cards will be included in the player class.
'''


def plus2yellow(player):
    print('Plus 2 yellow')
    player.yellow += 2
    player.capacity += 2
    return player


def upgrade_2(player):
    print('Select first crystal to upgrade.')
    upgrade1 = input().lower()
    player[f'{upgrade1}'] += 1
    print("Select second crystal to upgrade.")
    upgrade1 = input().lower()
    player[f'{upgrade1}'] += 1
    return player


def minus2yellow_plus2green(player):
    print('Trade 2 yellows for 2 greens.')
    player.yellow += -2
    player.green += 2
    player.blue += 0
    player.pink += 0
    player.capacity += 0
    return player


def minus2yellow_plus1blue(player):
    print('Trade 2 yellows for 1 blue.')
    player.yellow += -2
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.capacity += -1
    return player


def minus3yellow_plus1pink(player):
    print('Trade 3 yellows for 1 pink.')
    player.yellow += -3
    player.green += 0
    player.blue += 0
    player.pink += 1
    player.capacity += -2
    return player


def minus3yellow_plus1green1blue(player):
    print('Trade 3 yellow for 1 green and 1 blue.')
    player.yellow += -3
    player.green += 1
    player.blue += 1
    player.pink += 0
    player.capacity += -1
    return player


def minus4yellow_plus1blue1pink(player):
    print('Trade 4 yellow for 1 blue and 1 pink.')
    player.yellow += -4
    player.green += 0
    player.blue += 1
    player.pink += 1
    player.capacity += -2
    return player


def minus5yellow_plus2pink(player):
    print('Trade 5 yellow for 2 pink.')
    player.yellow += -5
    player.green += 0
    player.blue += 0
    player.pink += 2
    player.capacity += -3
    return player


def minus5yellow_plus3blue(player):
    print('Trade 5 yellow for 3 blue.')
    player.yellow += -5
    player.green += 0
    player.blue += 3
    player.pink += 0
    player.capacity += -2
    return player


def minus4yellow_plus2blue(player):
    print('Trade 4 yellow for 2 blue.')
    player.yellow += -4
    player.green += 0
    player.blue += 2
    player.pink += 0
    player.capacity += -2
    return player


def minus3yellow_plus3green(player):
    print('Trade 3 yellow for 3 green.')
    player.yellow += -3
    player.green += 3
    player.blue += 0
    player.pink += 0
    player.capacity += 0
    return player


def minus1green_plus3yellow(player):
    print('Trade 1 green for 3 yellow.')
    player.yellow += 3
    player.green += -1
    player.blue += 0
    player.pink += 0
    player.capacity += 2
    return player


def minus2green_plus2blue(player):
    print('Trade 2 green for 2 blue.')
    player.yellow += 0
    player.green += -2
    player.blue += 2
    player.pink += 0
    player.capacity += 0
    return player


def minus2green_plus1pink2yellow(player):
    print('Trade 2 green for 1 pink and 2 yellow.')
    player.yellow += 2
    player.green += -2
    player.blue += 0
    player.pink += 1
    player.capacity += 1
    return player


def minus2green_plus1blue3yellow(player):
    print('Trade 2 green for 1 blue 3 yellow.')
    player.yellow += 3
    player.green += -2
    player.blue += 1
    player.pink += 0
    player.capacity += 2
    return player


def minus3green_plus1pink1blue1yellow(player):
    print('Trade 3 green for 1 pink 1 blue and 1 yellow.')
    player.yellow += 1
    player.green += -3
    player.blue += 1
    player.pink += 1
    player.capacity += 0
    return player


def minus3green_plus2blue2yellow(player):
    print('Trade 3 green for 2 blue and 2 yellow.')
    player.yellow += 2
    player.green += -3
    player.blue += 2
    player.pink += 0
    player.capacity += 1
    return player


def minus3green_plus2pink(player):
    print('Trade 3 green for 2 pink.')
    player.yellow += 0
    player.green += -3
    player.blue += 0
    player.pink += 2
    player.capacity += -1
    return player


def minus3green_plus3blue(player):
    print('Trade 3 green for 3 blue.')
    player.yellow += 0
    player.green += -3
    player.blue += 3
    player.pink += 0
    player.capacity += 0
    return player


def minus1green1yellow_plus1pink(player):
    print('Trade 1 green and 1 yellow for 1 pink')
    player.yellow += -1
    player.green += -1
    player.blue += 0
    player.pink += 1
    player.capacity += -1
    return player


def minus1blue_plus2green(player):
    print('Trade 1 blue for 2 greens.')
    player.yellow += 0
    player.green += 2
    player.blue += -1
    player.pink += 0
    player.capacity += 1
    return player


def minus1blue_plus1green4yellow(player):
    print('Trade 1 blue for 1 green and 4 yellows.')
    player.yellow += 4
    player.green += 1
    player.blue += -1
    player.pink += 0
    player.capacity += 4
    return player


def minus1blue_plus2green1yellow(player):
    print('Trade 1 blue for 2 green and 1 yellow.')
    player.yellow += 1
    player.green += 2
    player.blue += -1
    player.pink += 0
    player.capacity += 2
    return player


def minus2blue_plus2pink(player):
    print('Trade 2 blue for 2 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += -2
    player.pink += 2
    player.capacity += 0
    return player


def minus2blue_plus1pink2green(player):
    print('Trade 2 blue for 1 pink and 2 green.')
    player.yellow += 0
    player.green += 2
    player.blue += -2
    player.pink += 1
    player.capacity += 1
    return player


def minus2blue_plus3green2yellow(player):
    print('Trade 2 blue for 3 green and 2 yellow.')
    player.yellow += 2
    player.green += 3
    player.blue += -2
    player.pink += 0
    player.capacity += 3
    return player


def minus2blue_plus1pink1green2yellow(player):
    print('Trade 2 blue for 1 pink, 1 green, and 2 yellow.')
    player.yellow += 2
    player.green += 1
    player.blue += -2
    player.pink += 1
    player.capacity += 2
    return player


def minus3blue_plus3pink(player):
    print('Trade 3 blue for 3 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += -3
    player.pink += 3
    player.capacity += 0
    return player


def minus1blue2yellow_plus2pink(player):
    print('Trade 1 blue and 2 yellow for 2 pink.')
    player.yellow += -2
    player.green += 0
    player.blue += -1
    player.pink += 2
    player.capacity += -1
    return player


def minus1pink_plus2blue(player):
    print('Trade 1 pink for 2 blue.')
    player.yellow += 0
    player.green += 0
    player.blue += 2
    player.pink += -1
    player.capacity += 1
    return player


def minus1pink_plus3green(player):
    print('Trade 1 pink for 3 green.')
    player.yellow += 0
    player.green += 3
    player.blue += 0
    player.pink += -1
    player.capacity += 2
    return player


def minus1pink_plus1blue1green1yellow(player):
    print('Trade 1 pink for 1 blue 1 green 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 1
    player.pink += -1
    player.capacity += 2
    return player


def minus1pink_plus2green2yellow(player):
    print('Trade 1 pink for 2 green 1 yellow.')
    player.yellow += 2
    player.green += 2
    player.blue += 0
    player.pink += -1
    player.capacity += 3
    return player


def minus1pink_plus1blue3yellow(player):
    print('Trade 1 pink for 1 blue and 3 yellow.')
    player.yellow += 3
    player.green += 0
    player.blue += 1
    player.pink += -1
    player.capacity += 3
    return player


def minus2pink_plus3blue1green1yellow(player):
    print('Trade 2 pink for 3 blue, 1 green, and 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 3
    player.pink += -2
    player.capacity += 3
    return player


def minus2pink_plus2blue3green(player):
    print('Trade 2 pink for 2 blue and 3 green.')
    player.yellow += 0
    player.green += 3
    player.blue += 2
    player.pink += -2
    player.capacity += 3
    return player


def plus3yellow(player):
    print('Gain 3 yellow.')
    player.yellow += 3
    player.green += 0
    player.blue += 0
    player.pink += 0
    player.capacity += 3
    return player


def plus4yellow(player):
    print('Gain 4 yellow.')
    player.yellow += 4
    player.green += 0
    player.blue += 0
    player.pink += 0
    player.capacity += 4
    return player


def plus1green1yellow(player):
    print('Gain 1 green and 1 yellow.')
    player.yellow += 1
    player.green += 1
    player.blue += 0
    player.pink += 0
    player.capacity += 2
    return player


def plus2green(player):
    print('Gain 2 green.')
    player.yellow += 0
    player.green += 2
    player.blue += 0
    player.pink += 0
    player.capacity += 2
    return player


def plus1blue(player):
    print('Gain 1 blue.')
    player.yellow += 0
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.capacity += 1
    return player


def plus1blue1yellow(player):
    print('Gain 1 blue and 1 yellow.')
    player.yellow += 1
    player.green += 0
    player.blue += 1
    player.pink += 0
    player.capacity += 2
    return player


def plus1pink(player):
    print('Gain 1 pink.')
    player.yellow += 0
    player.green += 0
    player.blue += 0
    player.pink += 1
    player.capacity += 1
    return player


def plus1green2yellow(player):
    print('Gain 1 green and 2 yellow.')
    player.yellow += 2
    player.green += 1
    player.blue += 0
    player.pink += 0
    player.capacity += 3
    return player


def upgrade3(player):
    print('Three total crystal upgrades.')
    print('Select first crystal to upgrade.')
    upgrade1 = input().lower()
    player[f'{upgrade1}'] += 1
    print("Select second crystal to upgrade.")
    upgrade1 = input().lower()
    player[f'{upgrade1}'] += 1
    print("Select third crystal to upgrade.")
    upgrade1 = input().lower()
    player[f'{upgrade1}'] += 1
    return player


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
