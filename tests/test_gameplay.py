import pytest
from pytest import mark


@mark.board
class TestBoard():
    '''
    This test suite will verify the Board class.
    '''

    def test_check_golem_board(self, create_player, create_board):
        ''''''
        board = create_board
        player = create_player
        print(board.golems_board)
        board.golems_board.pop()
        board.check_golem_board()
        print(board.golems_board)
