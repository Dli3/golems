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
# print(len(board.golems_list))
# print(board.golems_board)
# # print(board.actions_board)
# # Creating action cards board which contains 6 action cards at at time(or until deckout).
# del board.golems_board[0]

# print(board.golems_board)
# # print(board.actions_board)

# board.check_golem_board()
# print(len(board.golems_list))
# print(board.golems_board)
# del board.golems_board[0]
# board.check_golem_board()
# print(len(board.golems_list))

# print(board.actions_board)
# print(len(board.actions_list))
# del board.actions_board[0]
# print(board.actions_board)
# board.check_actions_board()
# print(len(board.actions_list))
# del board.actions_board[0]
# print(board.actions_board)
# board.check_actions_board()
# print(len(board.actions_list))
# print(board.actions_board)

# print(board.board_state())

print(actions_dict['minus3yellow_plus1pink'])
p = Player('dennis')
p.update_yellow(2)
p.update_blue(2)
# action_card(p, actions_dict['upgrade3'])
# print(p.yellow)
# print(p.green)
# p.hand[1](p)
# print(p.yellow)

# # minus2yellow_plus2green(p)

# print(p.yellow)
# print(p.green)


# p.yellow += 2
# p.green += 2
# p.blue += 2
# p.pink += 1

# capture_golem(board.golems_board, 1, p)
# print(p.points)
# print(board.golems_board)

# play_action(p, actions_dict)

print(p.yellow)
print(p.green)
print(p.blue)
print(p.pink)

print(p.hand)
print(p.discard_pile)
print(p.crystal_capacity)

print(board.actions_board_crystals[5])
print(board.actions_board)


# claim_action_card(board, p)
# play_action(p, actions_dict)
# print(p.discard_pile)
# print(p.hand)
# print(p.yellow)
# print(p.green)
# print(p.blue)
# print(p.pink)
# print(p.crystal_capacity)

# dicts = [
#     {'position': 'index_0', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0},
#     {'position': 'index_1', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0},
#     {'position': 'index_2', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0},
#     {'position': 'index_3', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0},
#     {'position': 'index_4', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0},
#     {'position': 'index_5', 'yellow': 0, 'green': 0, 'blue': 0, 'pink': 0}
# ]

# print(dicts)
# dicts[0]['green'] += 5
# print(dicts[0])

pay_for_action_card(board, p, 5)

print(board.actions_board_crystals)
