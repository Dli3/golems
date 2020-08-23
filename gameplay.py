'''
These functions are the gameplay actions.
'''
import random
from .players import Player
from .action_cards import actions_dict
from .golems import golems_cards

#! Initializing the game.


def define_number_of_players():
    '''
    Asking the user how many players are going to be playing this game of golems.
    Validation is in place to verify the a integer is specified between 1-5 players.
    '''
    while True:
        num_players = None
        while num_players != int and num_players not in range(1, 6):
            try:
                num_players = int(
                    input('This game can be played with 1-5 players. How many players are playing this round of golem?\n'))
            except ValueError:
                print('Sorry, please enter a valid number input between 1-5.')
                continue
        else:
            break
    print(f'Thank you! We have {num_players} players playing!\n')
    return num_players


def players_list():
    num_players = define_number_of_players()
    players_list = []
    for total_players in range(num_players):
        name = input(f'\nWhat is your name player {total_players + 1}?\n')
        players_list.append(Player(name))
    return players_list


def starting_hand(players_list):
    # Player 1
    if 0 in range(len(players_list)):
        starting_crystal = 3
        players_list[0].yellow += starting_crystal
        players_list[0].crystal_capacity += starting_crystal

    # Player 2
    if 1 in range(len(players_list)):
        starting_crystal = 4
        players_list[1].yellow += starting_crystal
        players_list[1].crystal_capacity += starting_crystal

    # Player 3
    if 2 in range(len(players_list)):
        starting_crystal = 4
        players_list[2].yellow += starting_crystal
        players_list[2].crystal_capacity += starting_crystal

    # Player 4
    if 3 in range(len(players_list)):
        starting_crystal_yellow = 3
        starting_crystal_green = 1
        starting_crystal_total = starting_crystal_yellow + starting_crystal_green

        players_list[3].yellow += 3
        players_list[3].green += 1
        players_list[3].crystal_capacity += starting_crystal_total

    # Player 5
    if 4 in range(len(players_list)):
        starting_crystal_yellow = 3
        starting_crystal_green = 1
        starting_crystal_total = starting_crystal_yellow + starting_crystal_green

        players_list[4].yellow += 3
        players_list[4].green += 1
        players_list[4].crystal_capacity += starting_crystal_total

    return players_list


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
# def rest(discard_pile, player_hand):
#     for card in discard_pile:
#         player_hand.append(card)
#     discard_pile.clear()
#     return player_hand
def rest(player):
    for card in player.check_discard_pile():
        player.hand.append(card)
        print(f"{card} returned to {player.name}'s hand.")
    player.discard_pile.clear()
    return player

# Play: play a card from their hand.


def play_action(player, actions_dict):
    '''
    Allows the player to play an action card from their hand. 

    Args:
        player: The player that's performing the action.
        actions_dict: The actions dictionary that the action cards reference. 
    '''
    print(f"\n{player.name}'s hand: {player.hand}")
    if len(player.hand) > 0:
        card_index = None
        while card_index != int:
            try:
                card_index = int(input(
                    f'Which action card would you like to play? Please enter the index between 0 and {len(player.hand )-1}.\n'))
                break
            except ValueError:
                print(
                    'ERROR: Please enter a valid input between 0 and {len(player.hand )-1}.\n')
        # player.hand[card_index](player)
        card = player.hand[card_index]
        print(card)
        action_card(player, card)
        player.discard_pile.append(player.hand[card_index])
        del player.hand[card_index]
    else:
        print(f"ERROR: Insufficent action cards in {player.name}'s hand.")
    return player


def action_card(player, action_key):
    if 'upgrade3' in str(action_key):
        actions_dict['upgrade3'](player)
    else:
        player.update_yellow(actions_dict[action_key][0])
        player.update_green(actions_dict[action_key][1])
        player.update_blue(actions_dict[action_key][2])
        player.update_pink(actions_dict[action_key][3])
        crystals = actions_dict[action_key][0] + actions_dict[action_key][1] + \
            actions_dict[action_key][2] + actions_dict[action_key][3]
        player.update_crystal_capacity(crystals)
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


# Claim: Acquire a golem.
def capture_golem(golem_board, player):
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

    golem_index = None
    while golem_index != int:
        try:
            golem_index = int(input(
                f'Which action card would you like to claim? Please enter the index between 0 and {len(golem_board)-1}.\n'))
            if golem_index not in range(0, 5):
                continue
        except ValueError:
            print(
                f'ERROR: Please enter valid input between 0-{len(golems_board)}.')
            continue
        break

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
    # Asking the player which action card they would like to claim from the actions board.
    card_index = None
    while card_index != int:
        try:
            card_index = int(input(
                f'Which action card would you like to claim? Please enter the index between 0 and {len(board.actions_board)-1}.\n'))
            if card_index not in range(0, 6):
                continue
        except ValueError:
            print(
                f'ERROR: Please enter valid input between 0-{len(board.actions_board)}.')
            continue
        break

    # If pay_for_action_card returns True, append the action card to player's hand.
    if pay_for_action_card(board, player, card_index) == True:
        player.update_hand(board.actions_board[card_index])
        # If there's crystals on the card index, the player also gains the crystals.
        if board.actions_board[card_index]['yellow'] > 0:
            player.update_yellow(board.actions_board[card_index]['yellow'])
            board.actions_board[card_index]['yellow'] = 0

        if board.actions_board[card_index]['green'] > 0:
            player.update_green(board.actions_board[card_index]['green'])
            board.actions_board[card_index]['green'] = 0

        if board.actions_board[card_index]['blue'] > 0:
            player.update_blue(board.actions_board[card_index]['blue'])
            board.actions_board[card_index]['blue'] = 0

        if board.actions_board[card_index]['pink'] > 0:
            player.update_pink(board.actions_board[card_index]['pink'])
            board.actions_board[card_index]['pink'] = 0

        del board.actions_board[card_index]


def pay_for_action_card(board, player, card_index):
    '''
    This function verifies the user has enough crystals to deposit in the indexes preceding the 
    action card they would like to claim. 

    Args:
        board: The board containing the action cards.
        player: The player attempting to claim the action card.
        card_index: The action card's index on the action board.
    '''
    crystal_count = player.check_total_crystals()
    print('Available number of crystals to spend: ' + str(crystal_count))

    claimable = True
    if crystal_count >= card_index - 1:
        for _ in range(card_index-1):
            crystal_paid = player.pay_in_crystals()
            board.actions_board_crystals[_][crystal_paid] += 1
        print(
            f'Successfully paid the crystal requirements for action card capture at index {card_index}.\n')
    else:
        print(
            f'ERROR: Insufficient crystal funds: {player.check_total_crystals()}\n')
        claimable = False
    return claimable


def take_a_turn(board, player):
    '''
    This function allows to player to select one out of the 4 turn options.
    Options: 
        1. Play: play a card from their hand.
        2. Acquire Action Card: Acquire a action card(merchant card).
        3. Rest: Take all previously played cards back to their hand.
        4. Claim: Acquire a golem.
    '''
    acceptable = ['a', 'b', 'c', 'd']
    moves = 1
    while moves > 0:
        choice = input(
            'What action would you like to make for your turn?\nOptions:\nA = Play action card\nB = Acquire an action card from the action card board\nC = Rest\nD = Claim a golem\n').lower()
        if choice in acceptable:
            if choice == 'a':
                play_action(player, actions_dict)
            elif choice == 'b':
                claim_action_card(board, player)
            elif choice == 'c':
                rest(player)
            elif choice == 'd':
                capture_golem(board, player)

        else:
            print('ERROR: Invalid input. Please enter a valid input.')
            continue
        moves -= 1
