from board import BoardRectangular
from Party import Party
from cartpt import CartPt
import pytest


def setup1_perform_board_assignments(board):
    board.setValueAtCartesian(CartPt(0, 0), Party.BLACK)
    board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    board.setValueAtCartesian(CartPt(0, 2), Party.NEUTRAL)

    board.setValueAtCartesian(CartPt(1, 0), Party.NEUTRAL)
    board.setValueAtCartesian(CartPt(1, 1), Party.WHITE)
    board.setValueAtCartesian(CartPt(1, 2), Party.NEUTRAL)

    board.setValueAtCartesian(CartPt(2, 0), Party.NEUTRAL)
    board.setValueAtCartesian(CartPt(2, 1), Party.NEUTRAL)
    board.setValueAtCartesian(CartPt(2, 2), Party.NEUTRAL)


def setup1_desired_state():
    return [
        Party.BLACK,
        Party.WHITE,
        Party.NEUTRAL,
        #
        Party.NEUTRAL,
        Party.WHITE,
        Party.NEUTRAL,
        #
        Party.NEUTRAL,
        Party.NEUTRAL,
        Party.NEUTRAL,
    ]


def test_board_init(default_board3x3, empty_states_default_board3x3):
    assert default_board3x3.state == empty_states_default_board3x3


def test_board_set_value_setup1(default_board3x3):
    setup1_perform_board_assignments(default_board3x3)
    desired_state = setup1_desired_state()
    assert default_board3x3.state == desired_state


def test_board_get_value_setup1(default_board3x3):
    setup1_perform_board_assignments(default_board3x3)
    assert default_board3x3.valueFromCartesian(CartPt(0, 0)) == Party.BLACK
    assert default_board3x3.valueFromCartesian(CartPt(1, 1)) == Party.WHITE
    assert default_board3x3.valueFromCartesian(CartPt(2, 2)) == Party.NEUTRAL
    assert default_board3x3.valueFromCartesian(CartPt(0, 1)) == Party.WHITE


def test_consistency_set_get(default_board3x3):
    board = default_board3x3
    setup1_perform_board_assignments(board)
    desired_state = setup1_desired_state()
    assert board.state == desired_state


def test_maximal_index_at_rectangular(default_board3x4):
    board = default_board3x4
    ROWS = default_board3x4.numOfRows()
    COLS = default_board3x4.numOfCols()
    board.setValueAtCartesian(CartPt(ROWS - 1, COLS - 1), Party.BLACK)
    assert board.valueFromCartesian(CartPt(ROWS - 1, COLS - 1)) == Party.BLACK


def test_index_exception_row(default_board3x4):
    """IndexError should be thrown if row index is number of rows or higher"""
    board = default_board3x4
    too_high_row_idx = board.numOfRows()
    with pytest.raises(IndexError):
        board.valueFromCartesian(CartPt(too_high_row_idx, 0))
    with pytest.raises(IndexError):
        board.valueFromCartesian(CartPt(-1, 0))


def test_getter_index_exception_col(default_board3x4):
    """IndexError should be thrown if col index is number of cols or higher"""
    board = default_board3x4
    too_high_col_idx = board.numOfCols()
    with pytest.raises(IndexError):
        board.valueFromCartesian(CartPt(0, too_high_col_idx))
    with pytest.raises(IndexError):
        board.valueFromCartesian(CartPt(0, -1))


def test_setter_index_exception_col(default_board3x4):
    """IndexError should be thrown if col index is number of cols or higher"""
    board = default_board3x4
    too_high_col_idx = board.numOfCols()
    with pytest.raises(IndexError):
        board.setValueAtCartesian(CartPt(too_high_col_idx, 0), Party.NEUTRAL)
    with pytest.raises(IndexError):
        board.setValueAtCartesian(CartPt(0, -1), Party.NEUTRAL)


def test_setter_index_exception_row(default_board3x4):
    """IndexError should be thrown if col index is number of cols or higher"""
    board = default_board3x4
    too_high_row_idx = board.numOfRows()
    with pytest.raises(IndexError):
        board.setValueAtCartesian(CartPt(too_high_row_idx, 0), Party.NEUTRAL)
    with pytest.raises(IndexError):
        board.setValueAtCartesian(CartPt(-1, 0), Party.NEUTRAL)


def test_board_to_string_does_not_fail(default_board3x3):
    setup1_perform_board_assignments(default_board3x3)
    outcome_string = str(default_board3x3)


def test_string_to_board(default_board3x3):
    string = "XXO\n___\nOO_"
    board = BoardRectangular.fromString(string)

    expected_board = default_board3x3
    expected_board.setValueAtCartesian(CartPt(0, 0), Party.WHITE)
    expected_board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    expected_board.setValueAtCartesian(CartPt(0, 2), Party.BLACK)

    expected_board.setValueAtCartesian(CartPt(1, 0), Party.NEUTRAL)
    expected_board.setValueAtCartesian(CartPt(1, 1), Party.NEUTRAL)
    expected_board.setValueAtCartesian(CartPt(1, 2), Party.NEUTRAL)

    expected_board.setValueAtCartesian(CartPt(2, 0), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(2, 1), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(2, 2), Party.NEUTRAL)

    for irow in range(0, 3):
        for icol in range(0, 3):
            assert (
                board.valueFromCartesian(CartPt(irow, icol)).value
                == expected_board.valueFromCartesian(CartPt(irow, icol)).value
            )


def test_string_to_board_invalid():
    string_varying_linelength = "XXO\n__\nOO_"
    with pytest.raises(ValueError):
        BoardRectangular.fromString(string_varying_linelength)


def test_set_from_cartesian2(default_board3x4):
    board = default_board3x4
    board.setValueAtCartesian(CartPt(0, 0), Party.NEUTRAL)
    board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    board.setValueAtCartesian(CartPt(0, 2), Party.BLACK)
    board.setValueAtCartesian(CartPt(0, 3), Party.NEUTRAL)

    board.setValueAtCartesian(CartPt(1, 0), Party.BLACK)
    board.setValueAtCartesian(CartPt(1, 1), Party.NEUTRAL)
    board.setValueAtCartesian(CartPt(1, 2), Party.BLACK)
    board.setValueAtCartesian(CartPt(1, 3), Party.NEUTRAL)

    board.setValueAtCartesian(CartPt(2, 0), Party.WHITE)
    board.setValueAtCartesian(CartPt(2, 1), Party.BLACK)
    board.setValueAtCartesian(CartPt(2, 2), Party.WHITE)
    board.setValueAtCartesian(CartPt(2, 3), Party.BLACK)
    expected_state = [
        Party.NEUTRAL,
        Party.WHITE,
        Party.BLACK,
        Party.NEUTRAL,
        Party.BLACK,
        Party.NEUTRAL,
        Party.BLACK,
        Party.NEUTRAL,
        Party.WHITE,
        Party.BLACK,
        Party.WHITE,
        Party.BLACK,
    ]
    assert board.state == expected_state


def test_string_to_board2(default_board3x4):
    expected_board = default_board3x4
    line0 = "_XO_\n"
    line1 = "O_O_\n"
    line2 = "XOXO"
    state_string = line0 + line1 + line2
    actual_board = BoardRectangular.fromString(state_string)
    expected_board.setValueAtCartesian(CartPt(0, 0), Party.NEUTRAL)
    expected_board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    expected_board.setValueAtCartesian(CartPt(0, 2), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(0, 3), Party.NEUTRAL)

    expected_board.setValueAtCartesian(CartPt(1, 0), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(1, 1), Party.NEUTRAL)
    expected_board.setValueAtCartesian(CartPt(1, 2), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(1, 3), Party.NEUTRAL)

    expected_board.setValueAtCartesian(CartPt(2, 0), Party.WHITE)
    expected_board.setValueAtCartesian(CartPt(2, 1), Party.BLACK)
    expected_board.setValueAtCartesian(CartPt(2, 2), Party.WHITE)
    expected_board.setValueAtCartesian(CartPt(2, 3), Party.BLACK)
    for irow in range(0, 3):
        for icol in range(0, 4):
            assert (
                actual_board.valueFromCartesian(CartPt(irow, icol)).value
                == expected_board.valueFromCartesian(CartPt(irow, icol)).value
            )
