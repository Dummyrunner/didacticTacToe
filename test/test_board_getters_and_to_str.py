from board import BoardRectangular
from Party import Party
from cartpt import CartPt
import pytest


def test_row_as_list(default_board3x4):
    board = default_board3x4
    board.setValueAtCartesian(CartPt(1, 0), Party.WHITE)
    board.setValueAtCartesian(CartPt(1, 1), Party.BLACK)
    board.setValueAtCartesian(CartPt(1, 2), Party.BLACK)
    actual = board.rowValsAsList(1)
    expected = [Party.WHITE, Party.BLACK, Party.BLACK, Party.NEUTRAL]
    assert actual == expected


def test_row_as_list_index_out_of_range(default_board3x4):
    board = default_board3x4
    with pytest.raises(IndexError):
        board.rowValsAsList(-1)
    with pytest.raises(IndexError):
        board.rowValsAsList(board.numOfRows())


def test_col_as_list(default_board3x4):
    board = default_board3x4
    board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    board.setValueAtCartesian(CartPt(1, 1), Party.BLACK)
    board.setValueAtCartesian(CartPt(2, 1), Party.BLACK)
    actual = board.colValsAsList(1)
    expected = [Party.WHITE, Party.BLACK, Party.BLACK]
    assert actual == expected


def test_col_as_list_index_out_of_range(default_board3x4):
    board = default_board3x4
    with pytest.raises(IndexError):
        board.colValsAsList(-1)
    with pytest.raises(IndexError):
        board.colValsAsList(board.numOfCols())


def test_maindiags_vals_as_list(default_board3x4):
    line0 = "_XO_\n"
    line1 = "O_O_\n"
    line2 = "_OXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    assert board.maindiagValsAsList(0) == [Party.NEUTRAL, Party.NEUTRAL, Party.WHITE]
    assert board.maindiagValsAsList(1) == [Party.WHITE, Party.BLACK, Party.BLACK]
    assert board.maindiagValsAsList(2) == [Party.BLACK, Party.NEUTRAL]
    assert board.maindiagValsAsList(3) == [Party.NEUTRAL]
    assert board.maindiagValsAsList(-1) == [Party.BLACK, Party.BLACK]
    assert board.maindiagValsAsList(-2) == [Party.NEUTRAL]
    with pytest.raises(IndexError):
        board.maindiagValsAsList(-3)
    with pytest.raises(IndexError):
        board.maindiagValsAsList(4)


def test_antidiags_vals_as_list(default_board3x4):
    line0 = "_OX_\n"
    line1 = "_O_O\n"
    line2 = "OXO_"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    assert board.antidiagValsAsList(0) == [Party.NEUTRAL, Party.NEUTRAL, Party.WHITE]
    assert board.antidiagValsAsList(1) == [Party.BLACK, Party.BLACK]
    assert board.antidiagValsAsList(2) == [Party.NEUTRAL]
    assert board.antidiagValsAsList(-1) == [Party.WHITE, Party.BLACK, Party.BLACK]
    assert board.antidiagValsAsList(-2) == [Party.BLACK, Party.NEUTRAL]
    assert board.antidiagValsAsList(-3) == [Party.NEUTRAL]
    with pytest.raises(IndexError):
        board.antidiagValsAsList(-4)


def test_get_row_assignemts_as_list(default_board3x4):
    board = default_board3x4
    board.setValueAtCartesian(CartPt(0, 1), Party.BLACK)
    board.setValueAtCartesian(CartPt(1, 2), Party.WHITE)
    assert board._getRowAssignmentsAsList(0) == [
        Party.NEUTRAL,
        Party.BLACK,
        Party.NEUTRAL,
        Party.NEUTRAL,
    ]
    assert board._getRowAssignmentsAsList(1) == [
        Party.NEUTRAL,
        Party.NEUTRAL,
        Party.WHITE,
        Party.NEUTRAL,
    ]
    assert board._getRowAssignmentsAsList(2) == [
        Party.NEUTRAL,
        Party.NEUTRAL,
        Party.NEUTRAL,
        Party.NEUTRAL,
    ]


def test_get_row_assignemts_as_list_fail(default_board3x4):
    board = default_board3x4
    with pytest.raises(IndexError):
        board._getRowAssignmentsAsList(-1)
    with pytest.raises(IndexError):
        board._getRowAssignmentsAsList(3)


def test_row_to_string(default_board3x4):
    board = default_board3x4
    board.setValueAtCartesian(CartPt(0, 1), Party.BLACK)
    board.setValueAtCartesian(CartPt(1, 2), Party.WHITE)
    assert board._rowToString(0) == "_O__"
    assert board._rowToString(1) == "__X_"
    with pytest.raises(IndexError):
        board._rowToString(-1)
    with pytest.raises(IndexError):
        board._rowToString(3)


def test_row_string_to_formatted():
    """check for number of occurence of each character:
    should be same in formatted and non-formatted line"""
    testline = "X__OXX"
    formatted = BoardRectangular._rowStringToFormatted(testline)
    for char in testline:
        assert formatted.count(char) == testline.count(char)


def test_row_string_to_formatted_short():
    testline = "XO"
    formatted = BoardRectangular._rowStringToFormatted(testline)
    assert testline == formatted


def test_game_dynamics_tictactoe_gravity_column__full():
    line0 = "X__\n"
    line1 = "O__\n"
    line2 = "OOX"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    assert board._columnFull(0) == True
    assert board._columnFull(1) == False
    assert board._columnFull(2) == False
