from action_cards import*
from players import *
from golem_cards import *
import random
from board import Board
from gameplay import*


def main():
    players = players_list()
    board = Board(players_list=players)

    board.check_golem_board()
    print(board.board_state())

    last_round = []

    while check_max_golems(players) != 5:
        for player in players:
            if check_max_golems(players) != 5:
                print(f"\n<===== PLAYER {player.name}'s TURN ======>")
                print(board.board_state())
                print(player.check_player_status())

                # Verifying Board state.
                board.check_golem_board()
                board.check_actions_board()

                # Player takes their turn.
                take_a_turn(board, player)
            else:
                for player in players:
                    if player.golems != 5:
                        last_round.append(player)

    # A player has reached 5 golems - Remaining players gets 1 last turn.
    for player in last_round:
        print(player)
        print(f"\n<===== PLAYER {player.name}'s TURN ======>")
        print(board.board_state())
        print(player.check_player_status())

        # Verifying Board state.
        board.check_golem_board()
        board.check_actions_board()

        # Player takes their turn.
        take_a_turn(board, player)

    # Counting up the player's points.
    winner = {'name': None,
              'points': 0}
    for player in players:
        if player.points > winner['points']:
            winner['name'] = player.name
            winner['points'] = player.points

    print(
        f"Congrats {winner['name']} on winning the game with {winner['points']} points!")


if __name__ == "__main__":
    main()
