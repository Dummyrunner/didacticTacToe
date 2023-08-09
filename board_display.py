from cartpt import CartPt
from Party import Party


class BoardDisplay:
    def _boardToString(self, board):
        res = "Board:\n"
        row_idx_range = range(0, board.numOfRows())
        col_idx_range = range(0, board.numOfCols())
        col_index_rows = self._colIndexRows(board)
        res += col_index_rows
        for irow in row_idx_range:
            res += self._rowIndexPrefix(irow, board)
            for icol in col_idx_range:
                char_to_add = board.state_markers_dict[
                    board.valueFromCartesian(CartPt(irow, icol))
                ]
                res += char_to_add
            if irow < board.numOfRows() - 1:
                res += "\n"
        res += 2 * "\n"
        res += self._markerLegend(board)
        return res

    def _rowIndexPrefix(self, row_idx, board):
        max_digits_index = BoardDisplay._numOfDigits(board.numOfRows() - 1)
        current_digit = BoardDisplay._numOfDigits(row_idx)
        empty_digits = max_digits_index - current_digit
        return empty_digits * " " + str(row_idx) + "|"

    def _colIndexRows(self, board):
        res = ""
        num_of_cols = board.numOfCols()
        max_digits_index = self._numOfDigits(num_of_cols - 1)
        col_idx_intendation = (
            BoardDisplay._numOfDigits(board.numOfCols() - 1) + 1
        ) * " "
        for digit in reversed(range(max_digits_index)):
            res += col_idx_intendation
            for col_idx in range(num_of_cols):
                if BoardDisplay._numOfDigits(col_idx) > digit:
                    res += str(BoardDisplay._nthDigit(col_idx, digit))
                else:
                    res += " "
            res += "\n"
        return res

    def _markerLegend(self, board):
        return (
            "\n"
            + "Marker for "
            + Party.WHITE.name
            + ": "
            + board.state_markers_dict[Party.WHITE]
            + ";\t"
            + "Marker for "
            + Party.BLACK.name
            + ": "
            + board.state_markers_dict[Party.BLACK]
        )

    @staticmethod
    def _rowStringToFormatted(rowstring):
        if len(rowstring) <= 2:
            return rowstring
        first_char = rowstring[0]
        last_char = rowstring[-1]
        interior_string = rowstring[1:-1]
        for i in range(len(interior_string) - 1, 0, -1):
            interior_string = interior_string[:i] + "|" + interior_string[i:]
        return first_char + "|" + interior_string + "|" + last_char

    @staticmethod
    def _numOfDigits(x):
        return len(str(x))

    @staticmethod
    def _nthDigit(x, n):
        x_str = str(x)
        max_idx = len(x_str) - 1
        if n >= len(x_str) or n < 0:
            raise AttributeError(
                "_nthDigit() Index "
                + str(n)
                + " out of Range! (Max idx would be "
                + str(len(x_str) - 1)
                + ")"
            )
        return int(x_str[max_idx - n])
