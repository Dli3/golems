import pytest
from pytest import mark


@mark.players
class Test_Players():
    '''
    This test suite will verify the Players class.
    '''

    def test_update_yellow(self, create_player):
        '''
        Verifying the update_yellow method under the Player class.
        The specified color and crystal_capacity should have the same result.
        Only the specified color and crystal_capacity should've been altered.
        '''
        player = create_player
        player.update_yellow(5)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 5
        assert player.yellow == 5
        assert player.green == 0
        assert player.blue == 0
        assert player.pink == 0

    def test_update_green(self, create_player):
        '''
        Verifying the update_green method under the Player class.
        The specified color and crystal_capacity should have the same result.
        Only the specified color and crystal_capacity should've been altered.
        '''
        player = create_player
        player.update_green(3)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 3
        assert player.yellow == 0
        assert player.green == 3
        assert player.blue == 0
        assert player.pink == 0

    def test_update_blue(self, create_player):
        '''
        Verifying the update_blue method under the Player class.
        The specified color and crystal_capacity should have the same result.
        Only the specified color and crystal_capacity should've been altered.
        '''
        player = create_player
        player.update_blue(2)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 2
        assert player.yellow == 0
        assert player.green == 0
        assert player.blue == 2
        assert player.pink == 0

    def test_update_pink(self, create_player):
        '''
        Verifying the update_pink method under the Player class.
        The specified color and crystal_capacity should have the same result.
        Only the specified color and crystal_capacity should've been altered.
        '''
        player = create_player
        player.update_pink(4)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 4
        assert player.yellow == 0
        assert player.green == 0
        assert player.blue == 0
        assert player.pink == 4

    def test_check_crystal_capacity(self, create_player):
        '''
        Verifying the check_crystal_capacity method under the Player class.
        If the player's crystal capacity is above 10, 
        the method will ask the user to remove crystal(s) of their choice
        until only 10 remains in their cart.
        '''
        player = create_player
        player.update_yellow(2)
        player.update_green(4)
        player.update_blue(2)
        player.update_pink(2)
        player.check_crystal_capacity()
        assert player.crystal_capacity == 10

    def test_check_total_crystals(self, create_player):
        '''
        Verifying the check_total_crystals method under the Player class.
        This method adds up the user's yellow, green, blue, and pink crystals
        and returns the total.
        '''
        player = create_player
        player.update_yellow(4)
        player.update_green(4)
        player.update_blue(4)
        player.update_pink(4)
        total = player.check_total_crystals()
        assert total == 16

    def test_pay_in_crystals(self, create_player):
        '''
        Verifying the pay_in_crystal method under the Player class.
        The user will be asked to pay in crystals when acquiring an
        action card(unless they're claiming index 0). 
        This test will verify the player's crystal count decreases 
        after payment.
        '''
        player = create_player
        player.update_yellow(2)
        player.update_green(4)
        player.update_blue(2)
        player.update_pink(2)
        current_total = player.crystal_capacity
        player.pay_in_crystals()
        assert player.crystal_capacity == current_total - 1
