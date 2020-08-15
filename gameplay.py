'''
These functions are the gameplay actions.
'''
import random
from players import Player
from action_cards import actions_dict
from golems import golems_cards

#! Initializing the game.


def define_number_of_players():
    '''
    Asking the user how many players are going to be playing this game of golems.
    Validation is in place to verify the a integer is specified between 1-5 players.
    '''
    while True:
        try:
            num_players = int(input('How many players?\n'))
        except ValueError:
            print('Sorry, please enter a valid number input between 1-5.')
            continue
        else:
            break
    while num_players not in range(1, 6):
        try:
            num_players = int(
                input('Please enter a valid number input between 1-5.\n'))
        except ValueError:
            print('Sorry, please enter a valid number input between 1-5.\n')
            continue
        else:
            break
    print(f'We have {num_players} players playing!\n')
    return num_players


def starting_hand(players_list):
    # Player 1
    if 0 in range(len(players_list)):
        players_list[0].yellow += 3
    # Player 2
    if 1 in range(len(players_list)):
        players_list[1].yellow += 4
    # Player 3
    if 2 in range(len(players_list)):
        players_list[2].yellow += 4
    # Player 4
    if 3 in range(len(players_list)):
        players_list[3].yellow += 3
        players_list[3].green += 1
    # Player 5
    if 4 in range(len(players_list)):
        players_list[4].yellow += 3
        players_list[4].green += 1
    return None


def create_golems_board(golems_list):
    '''
    Creates the golem board with 5 random golems from the golems list.
    The 5 randomly selected golems are then removed from the golems list.
    Returns the golem board.

    Args:
        golems_list: The list we're using to generate our golem board.
    '''
    golems_board = []
    for _ in range(5):
        random_golem = random.choice(golems_list)
        golems_board.append(random_golem)
        golems_list.remove(random_golem)
    return golems_board


def create_action_board(action_cards_list):
    '''
    Creates the action cards board with 6 randomly selected action cards from the 
    action cards list.
    Returns the action cards board.

    Args:
        action_cards_list: The list of action cards we're randomly selecting from.
    '''
    action_board = []
    for _ in range(6):
        random_action = (random.choice(action_cards_list))
        action_board.append(random_action)
        action_cards_list.remove(random_action)
    return action_board


#! Taking a turn actions
# There are 4 actions available to the player.
# 1. Play: play a card from their hand.
# 2. Acquire Action Card: Acquire a action card(merchant card).
# 3. Rest: Take all previously played cards back to their hand.
# 4. Claim: Acquire a golem.

def check_max_golems(players_list):
    '''
    Checks the golem count of each player provided in the players list.
    Returns the highest golem count.

    Args:
        players_list: The list of players playing the game.
    '''
    golems_count = [x.golems for x in players_list]
    return max(golems_count)

# Rest: Take all previously played cards back to their hand.


def rest(discard_pile, player_hand):
    for card in discard_pile:
        player_hand.append(card)
    discard_pile.clear()
    return player_hand

# Play: play a card from their hand.


def play_action(player, actions_dict):
    print(f"{player.name}'s hand: {player.hand}")
    card_index = None
    while card_index != int:
        card_index = int(input(
            f'Which action card would you like to play? Please enter the index between 0 and {len(player.hand )-1}.\n'))

    player.hand[card_index](player)
    player.discard_pile.append(player.hand[card_index])
    del player.hand[card_index]
    return player


def validate_player_crystals(actions_crystal, player):
    '''
    This function verifies that an action card doesn't result in a negative crystal count for 
    the player's yellow, green, blue, and pink.

    Args:
        actions_crystal: The action card dictionary key. This is specified from the player's hand. 
                          The list returned will be in the following order: [yellow, green, blue, pink]
        player: The player whose attempting to play the action card.
    '''
    player_arr = [player.yellow, player.green, player.blue, player.pink]

    zip_object = zip(player_arr, actions_crystal)
    results = []
    for player_crystal, action_crystal in zip_object:
        results.append(player_crystal - action_crystal)
    validated = True
    for result in results:
        if result < 0:
            validated = False
    return validated


def action_card(player, action_key):
    if 'upgrade3' in str(action_key):
        actions_dict['upgrade3'](player)
    else:
        player.update_yellow(action_key[0])
        player.update_green(action_key[1])
        player.update_blue(action_key[2])
        player.update_pink(action_key[3])
        crystals = action_key[0] + action_key[1] + \
            action_key[2] + action_key[3]
        player.update_crystal_capacity(crystals)

# Claim: Acquire a golem.


def capture_golem(golem_board, golem_index, player):
    '''
    This function verifies the crystals in the player's crystal cart meets the 
    requirements of the golem they're attempting to capture.
    Verifying the player's crystal count for each color doesn't reach a negative count.
    If the player meets the requirements, the crystals will be subtracted from the player's
    crystal cart and the golem count and score will be added to the player.

    Args:
        golem: The golem card they're trying to capture.
        player: The player trying to capture the golem.
    '''
    golem = golem_board[golem_index]
    print(f'\nAttempting to capture golem {golem}.')

    yellow = player.yellow - golems_cards[golem]['yellow'] if player.yellow - \
        golems_cards[golem]['yellow'] > -1 else False
    green = player.green - golems_cards[golem]['green'] if player.green - \
        golems_cards[golem]['green'] > -1 else False
    blue = player.blue - golems_cards[golem]['blue'] if player.blue - \
        golems_cards[golem]['blue'] > -1 else False
    pink = player.pink - golems_cards[golem]['pink'] if player.pink - \
        golems_cards[golem]['pink'] > -1 else False

    if yellow != False and green != False and blue != False and pink != False:
        player.update_yellow(yellow)
        player.update_green(green)
        player.update_blue(blue)
        player.update_pink(pink)
        player.update_golems()

        points = golems_cards[golem]['points']
        player.update_points(points)
        print(
            f'Congratulations! Player {player.name} captured {points} points.')
        golem_board.remove(golem)
    else:
        print('Sorry, you do not meet the golem requirements. \nMissing requirements:')
        if yellow == False:
            print(
                f'{str(player.yellow - golems_cards[golem]["yellow"])} Yellow Crystals')
        if green == False:
            print(
                f'{str(player.green - golems_cards[golem]["green"])} Green Crystals')
        if blue == False:
            print(
                f'{str(player.blue - golems_cards[golem]["blue"])} Blue Crystals')
        if pink == False:
            print(
                f'{str(player.pink - golems_cards[golem]["pink"])} Pink Crystals')
    return player, golem_board


# Acquire Action Card: Acquire a action card(merchant card).
def claim_action_card(board, player):
    '''
    This turn function allows a player to claim an action card 
    at the specified index on the board.actions_board list.
    The requirement to claim a card at a certain index is to drop a crystal for every index passed.
    We will check if the player has sufficient crystals to claim the card at the specified index.
    '''
    if pay_for_action_card(board, player):
        pass


def pay_for_action_card(board, player):
    crystal_count = player.crystal_sum()
    print(crystal_count)

    card_index = None
    while card_index != int:
        try:
            card_index = int(input(
                f'Which action card would you like to claim? Please enter the index between 1 and {len(board.actions_board)}.\n'))
        except ValueError:
            print(
                f'ERROR: Please enter valid input between 1-{len(board.actions_board)}.')
            continue
        break

    claimable = True
    if crystal_count >= card_index:
        for _ in range(card_index-1):
            player.pay_in_crystals()
            board.actions_board_crystals[_] += 1
    else:
        print(f'ERROR: Insufficient crystal funds: {player.crystal_sum()}')
        claimable = False
    print(board.actions_board_crystals)
    return claimable
