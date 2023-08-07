from board import BoardRectangular, BoardDisplay
import pytest


def test_board_display_num_of_digits():
    assert BoardDisplay._numOfDigits(555) == 3
    assert BoardDisplay._numOfDigits(0) == 1


def test_board_display_nth_digit():
    number = 12345
    assert BoardDisplay._nthDigit(number, 0) == 5
    assert BoardDisplay._nthDigit(number, 1) == 4
    assert BoardDisplay._nthDigit(number, 4) == 1
    with pytest.raises(AttributeError):
        BoardDisplay._nthDigit(number, -1)
    with pytest.raises(AttributeError):
        BoardDisplay._nthDigit(number, 5)


def test_board_display_col_index_rows():
    board = BoardRectangular(1, 12)
    line1 = "             11\n"
    line2 = "   012345678901\n"
    expected_res = line1 + line2
    actual_res = board.board_display._colIndexRows()
    assert actual_res == expected_res


def test_row_string_to_formatted():
    """check for number of occurence of each character:
    should be same in formatted and non-formatted line"""
    testline = "X__OXX"
    formatted = BoardDisplay._rowStringToFormatted(testline)
    for char in testline:
        assert formatted.count(char) == testline.count(char)


def test_row_string_to_formatted_short():
    testline = "XO"
    formatted = BoardDisplay._rowStringToFormatted(testline)
    assert testline == formatted
