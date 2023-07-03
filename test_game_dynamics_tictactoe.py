import pytest
from enum import Enum
from board import Board
from cartpt import CartPt
from Party import Party
from move_tictactoe import MoveTicTacToe

from axis import Axis
from game_dynamics_tictactoe import GameDynamicsTicTacToe

from human_player_tictactoe import HumanPlayerTicTacToe


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
    assert dynamics.maxLenCohesiveSeqInRowOfParty(0, Party.BLACK) == 1
    assert dynamics.maxLenCohesiveSeqInRowOfParty(1, Party.BLACK) == 3
    assert dynamics.maxLenCohesiveSeqInRowOfParty(2, Party.BLACK) == 2


def test_n_of_party_cohesive_seq_in_col():
    state_string = "OO_\n_OO\nOOO"
    board = Board.fromString(state_string)
    dynamics = GameDynamicsTicTacToe(board, 111)
    assert dynamics.maxLenCohesiveSeqInColOfParty(0, Party.BLACK) == 1
    assert dynamics.maxLenCohesiveSeqInColOfParty(1, Party.BLACK) == 3
    assert dynamics.maxLenCohesiveSeqInColOfParty(2, Party.BLACK) == 2


def test_has_party_won_at_axis_rows():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.ROW, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.ROW, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.ROW, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.ROW, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.ROW, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.ROW, Party.WHITE) == False


def test_has_party_won_at_axis_cols():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.COL, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.COL, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.COL, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(3, Axis.COL, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.COL, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.COL, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.COL, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(3, Axis.COL, Party.WHITE) == False


def test_has_party_won_at_axis_maindiags():
    line0 = "OXO_\n"
    line1 = "XOX_\n"
    line2 = "OXOX"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.MAINDIAG, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.MAINDIAG, Party.WHITE) == True
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(3, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(3, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-1, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-1, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-2, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-2, Axis.MAINDIAG, Party.WHITE) == False


def test_has_party_won_at_axis_antidiags():
    line0 = "OXOX\n"
    line1 = "XOX_\n"
    line2 = "OXOX"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(0, Axis.ANTIDIAG, Party.WHITE) == True
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(1, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(2, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-1, Axis.ANTIDIAG, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAxisByIndex(-1, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-2, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-2, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-3, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAxisByIndex(-3, Axis.ANTIDIAG, Party.WHITE) == False


def test_has_party_won_at_any_axis_antidiags():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWonAtAnyAxis(Axis.ROW, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.ROW, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.COL, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.COL, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.WHITE) == False


def test_has_party_won_game():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWon(Party.BLACK) == True
    assert dynamics.hasPartyWon(Party.WHITE) == False

    line0 = "OXOX\n"
    line1 = "X_OX\n"
    line2 = "_OXX"
    state_string = line0 + line1 + line2
    board2 = Board.fromString(state_string)
    rowsize_to_win = 3
    dynamics2 = GameDynamicsTicTacToe(board2, rowsize_to_win)

    assert dynamics2.hasPartyWon(Party.BLACK) == False
    assert dynamics2.hasPartyWon(Party.WHITE) == True
