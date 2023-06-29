import pytest
from enum import Enum
from board import Board, CartPt, Party
from game_dynamics_tictactoe import (
    GameDynamicsTicTacToe,
    HumanPlayerTicTacToe,
    MoveTicTacToe,
)


@pytest.fixture
def default_dynamics_tictactoe():
    board = Board(3, 3)
    rowsize_to_win = 3
    GameDynamicsTicTacToe(board, rowsize_to_win)
    return GameDynamicsTicTacToe(board, rowsize_to_win)


def test_doMoveOnBoard(default_dynamics_tictactoe):
    dynamics = default_dynamics_tictactoe
    board = dynamics.board
    center_square = CartPt(1, 1)
    corner_square = CartPt(2, 2)
    player_black = HumanPlayerTicTacToe(Party.BLACK)
    player_white = HumanPlayerTicTacToe(Party.WHITE)
    move_black_in_center = MoveTicTacToe(center_square, Party.BLACK)
    move_white_on_corner = MoveTicTacToe(corner_square, Party.WHITE)

    dynamics.doMoveOnBoard(player_black, move_black_in_center)
    dynamics.doMoveOnBoard(player_white, move_white_on_corner)

    assert board.valueFromCartesian(center_square) == Party.BLACK
    assert board.valueFromCartesian(corner_square) == Party.WHITE


def test_move_tictactoe_equality_overload():
    pt1 = CartPt(0, 0)
    pt2 = CartPt(0, 1)
    move1 = MoveTicTacToe(pt1, Party.BLACK)
    move2 = MoveTicTacToe(pt1, Party.WHITE)
    move3 = MoveTicTacToe(pt1, Party.WHITE)
    move4 = MoveTicTacToe(pt2, Party.BLACK)
    print(move1)
    print(move4)
    assert move2 == move3
    assert move1 != move2
    assert move1 != move3
    with pytest.raises(AssertionError):
        assert move1 == 333
