import pytest
from pytest import mark
from ..gameplay import *
from ..golems import golems_cards


@mark.gameplay
class TestGameplay():
    '''
    This test suite will verify the Gameplay class.
    '''

    @mark.skip(reason='Nothing is wrong, just skipping for now.')
    def test_define_number_of_players(self, create_player, create_board):
        '''
        Verifying the define_number_of_players function.
        '''
        player = create_player
        board = create_board
        num_of_players = define_number_of_players()
        assert num_of_players in range(1, 6)

    @mark.skip(reason='Nothing is wrong, just skipping for now.')
    def test_starting_hand(self):
        '''
        Verifying the starting_hand function.
        '''
        p_list = players_list()
        players = starting_hand(p_list)
        for player in players:
            player.crystal_count()

    def test_check_max_golems(self, create_player, create_player_2, create_board):
        '''
        Verifying the check_max_golems function.
        '''
        player_1 = create_player
        player_2 = create_player_2
        player_1.golems += 3
        player_2.golems += 5
        players_list = [player_1, player_2]

        max = check_max_golems(players_list)
        assert max == 5

    # @mark.skip
    def test_play_action(self, create_player):
        '''
        Testing the play_action function. 
        Verifying with plus2yellow that is in the player's starting hand.
        '''
        player = create_player
        player.check_total_crystals()
        play_action(player, actions_dict)  # Selecting index 1 for plus2yellow.
        assert player.yellow == 2
        assert player.crystal_capacity == 2
        player.check_total_crystals()

    def test_rest(self, create_player):
        player = create_player
