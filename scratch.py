from board import Board
from action_cards import*
from players import Player
from golems import golems_cards
import random
from gameplay import*

# The actions and golems list.
# golems_list = [golem for golem in golems_cards]
# action_list = [card for card in actions_dict]

# Creating golem board which contains 5 golems at a time(or until deckout).
# p = ['dennis', 'test']
board = Board()


p = Player('dennis')
p.update_yellow(2)
p.update_blue(2)

# take_a_turn()

board.board_state()
capture_golem(board.golems_board, p)
