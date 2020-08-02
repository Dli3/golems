def plus_two_yellow(crystal_cart):
    print('Plus 2 yellow')
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
    print('Trade 2 yellows for 2 greens.')
    crystal_cart['yellow'] += -2
    crystal_cart['green'] += 2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2yellow_plus1blue(crystal_cart):
    print('Trade 2 yellows for 1 blue.')
    crystal_cart['yellow'] += -2
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3yellow_plus1pink(crystal_cart):
    print('Trade 3 yellows for 1 pink.')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus3yellow_plus1green1blue(crystal_cart):
    print('Trade 3 yellow for 1 green and 1 blue.')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus4yellow_plus1blue1pink(crystal_cart):
    print('Trade 4 yellow for 1 blue and 1 pink.')
    crystal_cart['yellow'] += -4
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 1
    return crystal_cart


def minus5yellow_plus2pink(crystal_cart):
    print('Trade 5 yellow for 2 pink.')
    crystal_cart['yellow'] += -5
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 2
    return crystal_cart


def minus5yellow_plus3blue(crystal_cart):
    print('Trade 5 yellow for 3 blue.')
    crystal_cart['yellow'] += -5
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 3
    crystal_cart['pink'] += 0
    return crystal_cart


def minus4yellow_plus2blue(crystal_cart):
    print('Trade 4 yellow for 2 blue.')
    crystal_cart['yellow'] += -4
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3yellow_plus3green(crystal_cart):
    print('Trade 3 yellow for 3 green.')
    crystal_cart['yellow'] += -3
    crystal_cart['green'] += 3
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1green_plus3yellow(crystal_cart):
    print('Trade 1 green for 3 yellow.')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += -1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2green_plus2blue(crystal_cart):
    print('Trade 2 green for 2 blue.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2green_plus1pink2yellow(crystal_cart):
    print('Trade 2 green for 1 pink and 2 yellow.')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus2green_plus1blue3yellow(crystal_cart):
    print('Trade 2 green for 1 blue 3 yellow.')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += -2
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3green_plus1pink1blue1yellow(crystal_cart):
    print('Trade 3 green for 1 pink 1 blue and 1 yellow.')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 1
    return crystal_cart


def minus3green_plus2blue2yellow(crystal_cart):
    print('Trade 3 green for 2 blue and 2 yellow.')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus3green_plus2pink(crystal_cart):
    print('Trade 3 green for 2 pink.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 2
    return crystal_cart


def minus3green_plus3blue(crystal_cart):
    print('Trade 3 green for 3 blue.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += -3
    crystal_cart['blue'] += 3
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1green1yellow_plus1pink(crystal_cart):
    print('Trade 1 green and 1 yellow for 1 pink')
    crystal_cart['yellow'] += -1
    crystal_cart['green'] += -1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def minus1blue_plus2green(crystal_cart):
    print('Trade 1 blue for 2 greens.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1blue_plus1green4yellow(crystal_cart):
    print('Trade 1 blue for 1 green and 4 yellows.')
    crystal_cart['yellow'] += 4
    crystal_cart['green'] += 1
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus1blue_plus2green1yellow(crystal_cart):
    print('Trade 1 blue for 2 green and 1 yellow.')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2blue_plus2pink(crystal_cart):
    print('Trade 2 blue for 2 pink.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 2
    return crystal_cart


def minus2blue_plus1pink2green(crystal_cart):
    print('Trade 2 blue for 1 pink and 2 green.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 2
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 1
    return crystal_cart


def minus2blue_plus3green2yellow(crystal_cart):
    print('Trade 2 blue for 3 green and 2 yellow.')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 3
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 0
    return crystal_cart


def minus2blue_plus1pink1green2yellow(crystal_cart):
    print('Trade 2 blue for 1 pink, 1 green, and 2 yellow.')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 1
    crystal_cart['blue'] += -2
    crystal_cart['pink'] += 1
    return crystal_cart


def minus3blue_plus3pink(crystal_cart):
    print('Trade 3 blue for 3 pink.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += -3
    crystal_cart['pink'] += 3
    return crystal_cart


def minus1blue2yellow_plus2pink(crystal_cart):
    print('Trade 1 blue and 2 yellow for 2 pink.')
    crystal_cart['yellow'] += -2
    crystal_cart['green'] += 0
    crystal_cart['blue'] += -1
    crystal_cart['pink'] += 2
    return crystal_cart


def minus1pink_plus2blue(crystal_cart):
    print('Trade 1 pink for 2 blue.')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += -1
    return crystal_cart


def minus1pink_plus3green(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 3
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += -1
    return crystal_cart


def minus1pink_plus1blue1green1yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += -1
    return crystal_cart


def minus1pink_plus2green2yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += -1
    return crystal_cart


def minus1pink_plus1blue3yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += -1
    return crystal_cart


def minus2pink_plus3blue1green1yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 3
    crystal_cart['pink'] += -2
    return crystal_cart


def minus2pink_plus2blue3green(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 3
    crystal_cart['blue'] += 2
    crystal_cart['pink'] += -2
    return crystal_cart


def plus3yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 3
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def plus4yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 4
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def plus1green1yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def plus2green(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 2
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def plus1blue(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def plus1blue1yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 1
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 1
    crystal_cart['pink'] += 0
    return crystal_cart


def plus1pink(crystal_cart):
    print('')
    crystal_cart['yellow'] += 0
    crystal_cart['green'] += 0
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 1
    return crystal_cart


def plus1green2yellow(crystal_cart):
    print('')
    crystal_cart['yellow'] += 2
    crystal_cart['green'] += 1
    crystal_cart['blue'] += 0
    crystal_cart['pink'] += 0
    return crystal_cart


def upgrade3(crystal_cart):
    print('')
    print('Select one crystal to upgrade.')
    upgrade1 = input().lower()
    crystal_cart[f'{upgrade1}'] += 1
    print("Select second crystal to upgrade.")
    upgrade1 = input().lower()
    crystal_cart[f'{upgrade1}'] += 1
    print("Select second crystal to upgrade.")
    upgrade1 = input().lower()
    crystal_cart[f'{upgrade1}'] += 1
    return crystal_cart
