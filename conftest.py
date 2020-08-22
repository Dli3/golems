from pytest import fixture
from .players import Player
from .board import Board
from .gameplay import *


@fixture(autouse=True, scope='function')
def setup():
    pass


@fixture(scope='function')
def create_player():
    player = Player('Test Player 1')
    yield player


@fixture(scope='function')
def create_board():
    board = Board()
    yield board
