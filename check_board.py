'''
These functions are to check the board to verify the board gameplay state.
'''
import random


def verify_golem_count(player_name, player_golems):
    if player_golems > 5:
        print(f'Player {player_name} has achieved {player_golems} golems!')
        return True
    else:
        print(f'Player {player_name} has {player_golems} golems.')
        return False


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
