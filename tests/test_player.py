import pytest
from pytest import mark
from ..players import Player


def test_players():
    player = Player('Test Player')
    print(player.name)
