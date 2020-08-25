import pytest
from pytest import mark
import random


@mark.board
class TestBoard():
    '''
    This test suite will verify the Board class.
    '''

    def test_check_golem_board(self, create_player, create_board):
        ''''''
        board = create_board
        player = create_player

        before_golem_board = [golem for golem in board.golems_board]

        # Removing a random golem from the goles board.
        board.golems_board.pop(random.randrange(len(board.golems_board)))
        # Checking the length of the golem board and if less than 5, append a new golem from the golems list.
        board.check_golem_board()

        after_golem_board = [[golem for golem in board.golems_board]]

        # Verifying the board length after the method is 5.
        assert len(board.golems_board) == 5
        # Verifying the golem board doesn't contain the 5 same golems.
        assert before_golem_board != after_golem_board

    def test_check_actions_board(self, create_player, create_board):
        board = create_board
        player = create_player

        before_actions_board = [action for action in board.actions_board]
        board.actions_board.pop(random.randrange(len(board.actions_board)))

        board.check_actions_board()

        after_actions_board = [action for action in board.actions_board]

        assert len(board.actions_board) == 6

        assert before_actions_board != after_actions_board

    @mark.skip(reason='This only prints the state of the board. Unmark to see the board.')
    def test_board_state(self, create_player, create_board):
        board = create_board
        player = create_player
        board.board_state()

    def test_create_golems_board(self, create_board):
        '''
        Verifying the create_golems_board method under the Board class.
        '''
        board = create_board
        golems_board = board.create_golems_board()
        assert len(golems_board) == 5

    def test_create_action_board(self, create_board):
        '''
        Verifying the create_action_board method under the Board class.
        '''
        board = create_board
        golems_board = board.create_action_board()
        assert len(golems_board) == 6
