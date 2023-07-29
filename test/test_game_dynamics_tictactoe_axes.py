from board import BoardRectangular
from Party import Party
import pytest
from axis import Axis
from game_dynamics import GameDynamicsTicTacToe


def test_has_party_won_at_axis_rows():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.ROW, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.ROW, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.ROW, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.ROW, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.ROW, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.ROW, Party.WHITE) == False
    with pytest.raises(AttributeError):
        assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.KNOEDL, Party.WHITE) == False


def test_has_party_won_at_axis_cols():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.COL, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.COL, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.COL, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(3, Axis.COL, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.COL, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.COL, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.COL, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(3, Axis.COL, Party.WHITE) == False


def test_has_party_won_at_axis_maindiags():
    line0 = "OXO_\n"
    line1 = "XOX_\n"
    line2 = "OXOX"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.MAINDIAG, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.MAINDIAG, Party.WHITE) == True
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(3, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(3, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-1, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-1, Axis.MAINDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-2, Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-2, Axis.MAINDIAG, Party.WHITE) == False


def test_has_party_won_at_axis_antidiags():
    line0 = "OXOX\n"
    line1 = "XOX_\n"
    line2 = "OXOX"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(0, Axis.ANTIDIAG, Party.WHITE) == True
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(1, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(2, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-1, Axis.ANTIDIAG, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAxisByIndex(-1, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-2, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-2, Axis.ANTIDIAG, Party.WHITE) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-3, Axis.ANTIDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAxisByIndex(-3, Axis.ANTIDIAG, Party.WHITE) == False
