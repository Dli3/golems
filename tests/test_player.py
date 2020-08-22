import pytest
from pytest import mark
from ..players import Player


class Test_Players():

    def test_update_yellow(self):
        player = Player('Test Player')
        player.update_yellow(5)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 5
        assert player.yellow == 5
        assert player.green == 0
        assert player.blue == 0
        assert player.pink == 0

    def test_update_green(self):
        player = Player('Test Player')
        player.update_green(3)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 3
        assert player.yellow == 0
        assert player.green == 3
        assert player.blue == 0
        assert player.pink == 0

    def test_update_blue(self):
        player = Player('Test Player')
        player.update_blue(2)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 2
        assert player.yellow == 0
        assert player.green == 0
        assert player.blue == 2
        assert player.pink == 0

    def test_update_pink(self):
        player = Player('Test Player')
        player.update_pink(4)
        assert player.points == 0
        assert player.golems == 0
        assert player.crystal_capacity == 4
        assert player.yellow == 0
        assert player.green == 0
        assert player.blue == 0
        assert player.pink == 4

    def test_check_crystal_capacity(self):
        player = Player('Test Player')
        player.update_yellow(2)
        player.update_green(4)
        player.update_blue(2)
        player.update_pink(2)
        player.check_crystal_capacity()
        assert player.crystal_capacity == 10

    def test_check_total_crystals(self):
        player = Player('Test Player')
        player.update_yellow(4)
        player.update_green(4)
        player.update_blue(4)
        player.update_pink(4)
        total = player.check_total_crystals()
        assert total == 16

    def test_pay_in_crystals(self):
        player = Player('Test Player')
        player.update_yellow(2)
        player.update_green(4)
        player.update_blue(2)
        player.update_pink(2)
        current_total = player.crystal_capacity
        player.pay_in_crystals()
        assert player.crystal_capacity == current_total - 1
