import pytest
from pytest import mark
from ..action_cards import *


@mark.actions
class Test_Actions():
    '''
    This test suite will verify the action cards functions.
    '''

    def test_upgrade(self, create_player):
        player = create_player
        assert player.yellow == 0
        assert player.green == 0
        assert player.blue == 0
        assert player.pink == 0

        current_total = player.yellow + player.green + player.blue + player.pink
        player.update_yellow(1)
        upgrade(player)
        new_total = player.yellow + player.green + player.blue + player.pink

        assert current_total != new_total
