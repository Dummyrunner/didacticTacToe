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
    assert move2 == move3
    assert move1 != move2
    assert move1 != move3
    with pytest.raises(AssertionError):
        assert move1 == 333


def test_n_of_party_cohesive_seq_in_row():
    state_string = "O_O\nOOO\n_OO"
    board = Board.fromString(state_string)
    dynamics = GameDynamicsTicTacToe(board, 111)
    assert dynamics.cohesiveSeqInRowOfParty(0, Party.BLACK) == 1
    assert dynamics.cohesiveSeqInRowOfParty(1, Party.BLACK) == 3
    assert dynamics.cohesiveSeqInRowOfParty(2, Party.BLACK) == 2


def test_n_of_party_cohesive_seq_in_col():
    state_string = "OO_\n_OO\nOOO"
    board = Board.fromString(state_string)
    print(board)
    dynamics = GameDynamicsTicTacToe(board, 111)
    assert dynamics.cohesiveSeqInColOfParty(0, Party.BLACK) == 1
    assert dynamics.cohesiveSeqInColOfParty(1, Party.BLACK) == 3
    assert dynamics.cohesiveSeqInColOfParty(2, Party.BLACK) == 2
