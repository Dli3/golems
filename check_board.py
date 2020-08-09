'''
These functions are to check the board to verify the board gameplay state.
'''
import random
from players import Player


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


#! Turn actions
def check_max_golems(players_list):
    '''
    Checks the golem count of each player provided in the players list.
    Returns the highest golem count.

    Args:
        players_list: The list of players playing the game.
    '''
    golems_count = [x.golems for x in players_list]
    return max(golems_count)


def capture_golem(golem_requirement, player):
    '''
    This function verifies the crystals in the player's crystal cart meets the 
    requirements of the golem they're attempting to capture.
    Verifying the player's crystal count for each color doesn't reach a negative count.
    If the player meets the requirements, the crystals will be subtracted from the player's
    crystal cart and the golem count and score will be added to the player.

    Args:
        golem_requirement: The golem card they're trying to capture.
        player: The player trying to capture the golem.
    '''
    yellow = player.yellow - golem_requirement.yellow if player.yellow - \
        golem_requirement.yellow > -1 else False
    green = player.green - golem_requirement.green if player.green - \
        golem_requirement.green > -1 else False
    blue = player.blue - golem_requirement.blue if player.blue - \
        golem_requirement.blue > -1 else False
    pink = player.pink - golem_requirement.pink if player.pink - \
        golem_requirement.pink > -1 else False

    if yellow != False and green != False and blue != False and pink != False:
        player.yellow = yellow
        player.green = green
        player.blue = blue
        player.pink = pink
        player.golems += 1
        player.score += golem_requirement.points
    else:
        print('Sorry, you do not meet the golem requirements. \n Missing requirements:')
        if yellow == False:
            print('Yellow Crystals')
        if green == False:
            print('Green Crystals')
        if blue == False:
            print('Blue Crystals')
        if pink == False:
            print('Pink Crystals')
    return player
