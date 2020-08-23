import pytest
from pytest import mark
from ..gameplay import *


@mark.gameplay
class TestGameplay():
    '''
    This test suite will verify the Gameplay class.
    '''

    @mark.skip(reason='Nothing is wrong, just skipping for now.')
    def test_define_number_of_players(self, create_player, create_board):
        player = create_player
        board = create_board
        num_of_players = define_number_of_players()
        assert num_of_players in range(1, 6)

    @mark.skip(reason='Nothing is wrong, just skipping for now.')
    def test_starting_hand(self):
        p_list = players_list()
        players = starting_hand(p_list)
        for player in players:
            player.crystal_count()
