from board import Board
from action_cards import*
from players import Player
from golems import golems_cards
import random
from check_board import*

# The actions and golems list.
# golems_list = [golem for golem in golems_cards]
# action_list = [card for card in actions_dict]

# Creating golem board which contains 5 golems at a time(or until deckout).
p = ['dennis', 'test']
board = Board(players_list=p)
print(len(board.golems_list))
print(board.golems_board)
# print(board.actions_board)
# Creating action cards board which contains 6 action cards at at time(or until deckout).
del board.golems_board[0]

print(board.golems_board)
# print(board.actions_board)

board.check_golem_board()
print(len(board.golems_list))
print(board.golems_board)
del board.golems_board[0]
board.check_golem_board()
print(len(board.golems_list))

print(board.actions_board)
print(len(board.actions_list))
del board.actions_board[0]
print(board.actions_board)
board.check_actions_board()
print(len(board.actions_list))
del board.actions_board[0]
print(board.actions_board)
board.check_actions_board()
print(len(board.actions_list))
print(board.actions_board)

print(board.board_state())
