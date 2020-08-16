from gameplay import*
from golems import*
from action_cards import*
import random


class Board():
    def __init__(self, **players_list):
        self.golems_list = [golem for golem in golems_cards]
        self.actions_list = [card for card in actions_dict]

        self.actions_board = create_action_board(self.actions_list)
        self.actions_board_crystals = [0, 0, 0, 0, 0, 15]
        self.golems_board = create_golems_board(self.golems_list)
        self.players_list = players_list

    def check_golem_board(self):
        '''
        Checks the golem board has 5 golems. 
        If the golem board has less than 5 golems, a random golem will be
        randomly selected from the golems list and added to the golems board.
        The selected golem will then be removed from the golems list.
        Returns the golem board.
        '''
        if len(self.golems_board) < 5:
            random_golem = random.choice(self.golems_list)
            self.golems_board.append(random_golem)
            self.golems_list.remove(random_golem)

        # Assigning coins per each player times 2 and attaching it to the golem at index 0 and 1 if coin count isn't 0.
        copper_coin = len(self.players_list) * 2
        silver_coin = len(self.players_list) * 2

        if golems_cards[self.golems_board[0]]['copper_coins'] == 0:
            golems_cards[self.golems_board[0]]['copper_coins'] += copper_coin

        if golems_cards[self.golems_board[1]]['silver_coins'] == 0:
            golems_cards[self.golems_board[1]]['silver_coins'] += silver_coin

        return self.golems_board

    def check_actions_board(self):
        '''
        Checks the actions board to verify there's 6 action cards at the start of every player's turn.
        '''
        if len(self.actions_board) < 6:
            random_action = (random.choice(self.actions_list))
            self.actions_board.append(random_action)
            self.actions_list.remove(random_action)
        return self.actions_board

    def board_state(self):
        print(f'\nGolems Board:\nCount: {len(self.golems_board)}')
        for golem in self.golems_board:
            print(golem, golems_cards[golem])

        print(f'\nAction Cards Board:\nCount: {len(self.actions_board)}')
        for action in self.actions_board:
            print(action)
