def plus_two_yellow(crystal_cart):
    print('+ 2 yellow')
    crystal_cart['yellow'] += 2
    return crystal_cart


def upgrade_two(crystal_cart):
    print('Select one crystal to upgrade.')
    upgrade1 = input().lower()
    crystal_cart[f'{upgrade1}'] += 1
    print("Select second crystal to upgrade.")
    upgrade1 = input().lower()
    crystal_cart[f'{upgrade1}'] += 1
    return crystal_cart


def minus2yellow_plus2green(crystal_cart):
    print('Trade 2 yellows for 2 greens: -2 yellow + 2 green')
    crystal_cart['yellow'] += -2
    crystal_cart['green'] += 2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2yellow_plus1blue(crystal_cart):
    print('Trade 2 yellows for 1 blue: -2 yellow + 1 blue')
    crystal_cart['yellow'] += -2
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3yellow_plus1pink(crystal_cart):
    print('Trade 3 yellows for 1 pink: -3 yellow + 1 pink')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus3yellow_plus1green1blue(crystal_cart):
    print('Trade 3 yellow for 1 green and 1 blue: -3 yellow + 1 green + 1 blue')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus4yellow_plus1blue1pink(crystal_cart):
    print('Trade 4 yellow for 1 blue and 1 pink: -4 yellow + 1 blue + 1 pink')
    crystal_cart['yellow'] += -4
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 1
    return crystal_cart


def minus5yellow_plus2pink(crystal_cart):
    print('Trade 5 yellow for 2 pink: -5 yellow + 2 pink')
    crystal_cart['yellow'] += -5
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 2
    return crystal_cart


def minus5yellow_plus3blue(crystal_cart):
    print('Trade 5 yellow for 3 blue: -5 yellow + 3 blue')
    crystal_cart['yellow'] += -5
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 3
    crystal_cart['pink'] += 0
    return crystal_cart


def minus4yellow_plus2blue(crystal_cart):
    print('Trade 4 yellow for 2 blue: -4 yellow + 2 blue')
    crystal_cart['yellow'] += -4
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3yellow_plus3green(crystal_cart):
    print('Trade 3 yellow for 3 green: -3 yellow + 3 green')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 3
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1green_plus3yellow(crystal_cart):
    print('Trade 1 green for 3 yellow: -1 green + 3 yellow')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += -1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2green_plus2blue(crystal_cart):
    print('Trade 2 green for 2 blue: -2 green + 2 blue')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2green_plus1pink2yellow(crystal_cart):
    print('Trade 2 green for 1 pink and 2 yellow: -2 green + 1 pink + 2 yellow')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus2green_plus1blue3yellow(crystal_cart):
    print('Trade 2 green for 1 blue 3 yellow: -2 green + 1 blue + 3 yellow')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3green_plus1pink1blue1yellow(crystal_cart):
    print('Trade 3 green for 1 pink 1 blue and 1 yellow')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 1
    return crystal_cart


def minus3green_plus2blue2yellow(crystal_cart):
    print('Trade 3 green for 2 blue and 2 yellow: -3 green + 2 blue + 2 yellow')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3green_plus2pink(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 2
    return crystal_cart


def minus3green_plus3blue(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 3
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1green1yellow_plus1pink(crystal_cart):
    print('')
    crystal_cart['yellow'] += -1
    crystal_cart['green'] += -1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus1blue_plus2green(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1blue_plus1green4yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 4
    crystal_cart['green'] += 1
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1blue_plus2green1yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2blue_plus2pink(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 2
    return crystal_cart


def minus2blue_plus1pink2green(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 1
    return crystal_cart


def minus2blue_plus3green2yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 3
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2blue_plus1red1green2yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 1
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 1
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def _(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart
