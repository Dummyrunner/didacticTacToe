from move import MoveTicTacToe, MoveBase
from cartpt import CartPt
from Party import Party
import pytest


def test_move_base_init():
    try:
        move = MoveBase(Party.WHITE)
    except:
        pytest.fail("initializing of MoveBase leads to exception!")
    move_black = MoveBase(Party.BLACK)
    move_white = MoveBase(Party.WHITE)
    move_neutral = MoveBase(Party.NEUTRAL)
    assert move_black.party == Party.BLACK
    assert move_white.party == Party.WHITE
    assert move_neutral.party == Party.NEUTRAL


def test_move_tictactoe_init():
    try:
        move = MoveTicTacToe(CartPt(1, 2), Party.WHITE)
    except:
        pytest.fail("initializing of MoveTicTacToe leads to exception!")
    assert move.party == Party.WHITE
    assert move.cartpt_to_fill == CartPt(1, 2)


def test_move_tictactoe_print_without_throw():
    move_white = MoveTicTacToe(CartPt(1, 2), Party.WHITE)
    move_black = MoveTicTacToe(CartPt(1, 2), Party.BLACK)
    move_neutral = MoveTicTacToe(CartPt(1, 2), Party.NEUTRAL)
    assert type(str(move_white)) == str
    assert type(str(move_black)) == str
    assert type(str(move_neutral)) == str


def test_move_tictactoe_equality_overload():
    pt1 = CartPt(0, 0)
    pt2 = CartPt(0, 1)
    move1 = MoveTicTacToe(pt1, Party.BLACK)
    move2 = MoveTicTacToe(pt1, Party.WHITE)
    move3 = MoveTicTacToe(pt1, Party.WHITE)
    move4 = MoveTicTacToe(pt2, Party.WHITE)
    assert move2 == move3
    assert move1 != move2
    assert move1 != move3
    assert move4 != move2
    with pytest.raises(AssertionError):
        assert move1 == 333


def test_move_tictactoe_hash():
    pt1 = CartPt(0, 0)
    pt2 = CartPt(0, 1)
    move1 = MoveTicTacToe(pt1, Party.BLACK)
    move2 = MoveTicTacToe(pt1, Party.WHITE)
    move3 = MoveTicTacToe(pt2, Party.BLACK)
    move4 = MoveTicTacToe(pt1, Party.BLACK)
    assert hash(move1) == hash(move4)
    assert hash(move1) != hash(move2)
    assert hash(move1) != hash(move3)
