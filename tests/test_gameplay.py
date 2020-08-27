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

    @mark.skip
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

    @mark.skip
    def test_rest(self, create_player):
        '''
        Testing the rest function that should return all cards in the discard pile to the player's hand.
        Using the play_action function to move the 2 starter cards
        from the player's hand into the player's graveyard.
        '''
        player = create_player
        assert len(player.hand) == 2
        assert len(player.discard_pile) == 0

        play_action(player)
        play_action(player)

        assert len(player.hand) == 0
        assert len(player.discard_pile) == 0

        rest(player)
        assert len(player.hand) == 2
        assert len(player.discard_pile) == 0

    def test_action_card(self, create_player, create_board):
        player = create_player
        assert player.crystal_capacity_counter() == 0

        action_card(player, 'minus2yellow_plus2green')
        player.crystal_capacity_counter()
