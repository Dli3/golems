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
                take_a_turn(board, player)
            else:
                for player in players:
                    if player.golems != 5:
                        last_round.append(player)

    for player in last_round:
        print(player)


if __name__ == "__main__":
    main()
