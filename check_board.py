'''
These functions are to check the board to verify the board gameplay state.
'''
import random
from players import Player


def verify_golem_count(player_name, player_golems):
    if player_golems > 5:
        print(f'Player {player_name} has achieved {player_golems} golems!')
        return True
    else:
        print(f'Player {player_name} has {player_golems} golems.')
        return False


def check_max_golems(players_list):
    golems_count = [x.golems for x in players_list]
    return max(golems_count)


def create_golems_board(golems_list):
    golems_board = []
    for _ in range(5):
        random_golem = random.choice(golems_list)
        golems_board.append(random_golem)
        golems_list.remove(random_golem)
    return golems_board


def check_golem_board(golems_list, golems_board):
    if len(golems_board) < 5:
        random_golem = random.choice(golems_list)
        golems_board.append(random_golem)
        golems_list.remove(random_golem)
    return golems_board


# Turn actions
def capture_golem(player, index_position, golems_board, crystal_cart, golem_cards):
    print(golems_board[index_position])

    print(golem_cards[golems_board[index_position]]['requirements'])
    # if golem_cards[golems_board[index_position]]['requirements'] in crystal_cart:
    print(crystal_cart)
    result = {key: crystal_cart[key] - golem_cards[golems_board[index_position]]['requirements'].get(key, 0)
              for key in crystal_cart[key]}
    print(result)


def define_number_of_players():
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
    print(f'We have {num_players} players playing!')
    return num_players
