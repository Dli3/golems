'''
These functions are to check the board to verify the board gameplay state.
'''


def verify_golem_count(player_name, player_golems):
    if player_golems > 5:
        print(f'Player {player_name} has achieved {player_golems} golems!')
        return True
    else:
        print(f'Player {player_name} has {player_golems} golems.')
        return False
