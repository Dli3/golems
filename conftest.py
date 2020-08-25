from pytest import fixture
from .players import Player
from .board import Board
from .gameplay import *


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
