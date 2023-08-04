from move import MoveTicTacToeGravity
from Party import Party
import pytest


def test_move_tictactoe_gravity_init():
    move_black = MoveTicTacToeGravity(1, Party.BLACK)
    move_white = MoveTicTacToeGravity(2, Party.WHITE)
    move_neutral = MoveTicTacToeGravity(3, Party.NEUTRAL)
    assert move_black.party == Party.BLACK
    assert move_white.party == Party.WHITE
    assert move_neutral.party == Party.NEUTRAL
    assert move_black.target_column == 1
    assert move_white.target_column == 2
    assert move_neutral.target_column == 3


def test_move_tictactoe_gravity_init_fail():
    try:
        move = MoveTicTacToeGravity(2, Party.WHITE)
    except:
        pytest.fail("initializing of MoveBase leads to exception!")
    with pytest.raises(AttributeError):
        move = MoveTicTacToeGravity("wrongtype", Party.WHITE)


def test_move_tictactoe_gravity_equality_overload():
    col1 = 0
    col2 = 1
    move1 = MoveTicTacToeGravity(col1, Party.BLACK)
    move2 = MoveTicTacToeGravity(col1, Party.WHITE)
    move3 = MoveTicTacToeGravity(col1, Party.WHITE)
    move4 = MoveTicTacToeGravity(col2, Party.WHITE)
    assert move2 == move3
    assert move1 != move2
    assert move1 != move3
    assert move4 != move2
    with pytest.raises(AssertionError):
        assert move1 == 333


def test_move_tictactoe_gravity_hash():
    col1 = 0
    col2 = 1
    move1 = MoveTicTacToeGravity(col1, Party.BLACK)
    move2 = MoveTicTacToeGravity(col1, Party.WHITE)
    move3 = MoveTicTacToeGravity(col2, Party.BLACK)
    move4 = MoveTicTacToeGravity(col1, Party.BLACK)
    assert hash(move1) == hash(move4)
    assert hash(move1) != hash(move2)
    assert hash(move1) != hash(move3)
