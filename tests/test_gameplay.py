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
        '''
        Testing the action_card function. 
        Shouldn't allow the player to play the card if there's insufficient crystals.
        '''
        #! Creating the player which starts off with 0 crystals.
        player = create_player
        assert player.crystal_capacity_counter() == 0

        #! Expected result: Unable to play card.
        action_card(player, 'minus2yellow_plus2green')
        assert player.crystal_capacity_counter() == 0

        #! Expected result: Successfully added 2 yellow crystals but unable to play the 2nd card that exceeds funds.
        action_card(player, 'plus2yellow')
        assert player.crystal_capacity_counter() == 2
        action_card(player, 'minus5yellow_plus2pink')
        assert player.crystal_capacity_counter() == 2

        #! Expected result: Successfully adds 3 yellow crystal and is able to play 2nd card now that there's sufficient funds.
        action_card(player, 'plus3yellow')
        assert player.crystal_capacity_counter() == 5
        action_card(player, 'minus5yellow_plus2pink')
        assert player.crystal_capacity_counter() == 2

    def test_crystal_validation(self, create_player):
        '''
        Testing the crystal_validation function.
        Returns True if none of the results returns negative. 
        Returns False if any of the results return negative.
        '''
        player = create_player

        assert crystal_validation(
            actions_dict['plus3yellow'], player) == True
        assert crystal_validation(
            actions_dict['minus3green_plus2pink'], player) == False
        assert crystal_validation(
            actions_dict['minus1green1yellow_plus1pink'], player) == False

    @mark.skip
    def test_capture_golem(self, create_player, create_board):
        '''
        Verifying the capture_golems function.
        '''
        player = create_player
        board = create_board
        golems_board = board.create_golems_board()
        print(golems_board)

        #! Attempting to capture a golem without sufficient crystal funds.
        assert player.golems == 0
        capture_golem(golems_board, player)
        assert player.golems == 0

        player.update_yellow(5)
        player.update_green(5)
        player.update_blue(5)
        player.update_pink(5)
        capture_golem(golems_board, player)

        assert player.golems == 1

    @mark.skip
    def test_pay_for_action_card(self, create_player, create_board):
        player = create_player
        board = create_board
        player.update_yellow(4)
        player.update_green(2)
        player.update_blue(1)
        # print(board.actions_board)
        pay_for_action_card(board, player)
        print(board.actions_board_crystals)

    @mark.skip
    def test_claim_action_card(self, create_player, create_board):
        player = create_player
        board = create_board
        assert len(player.hand) == 2
        player.update_yellow(4)
        player.update_green(2)
        player.update_blue(1)
        print(board.actions_board)

        claim_action_card(board, player)
        print(player.hand)
        print(board.actions_board)

        assert len(player.hand) == 3
        assert len(board.actions_board) == 5

    def test_take_a_turn(self, create_player, create_board):
        player = create_player
        board = create_board

        take_a_turn(board, player)
        # take_a_turn(board, player)
