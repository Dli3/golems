from pytest import fixture
from golems.players import *
from golems.board import *
from golems.gameplay import *


@fixture(autouse=True, scope='function')
def setup():
    return None


@fixture(scope='function')
def create_player(name='Test Player 1'):
    player = Player(name)
    yield player


@fixture(scope='function')
def create_player_2(name='Test Player 2'):
    player = Player(name)
    yield player


@fixture(scope='function')
def create_board():
    board = Board()
    yield board
