from enum import Enum
from cartpt import CartPt
from Party import Party


class Board:
    """Board Rectangular gameboard.

    Parameters:
            state_markers_dict (dict): game parties (by default BLACK, WHITE, NEUTRAL)to corresponding board character

            size_x (int): Boardwidth in squares
            size_y (int): Boardheight in squares"""

    def __init__(
        self,
        size_x=3,
        size_y=3,
        markers_dict={Party.NEUTRAL: "_", Party.BLACK: "O", Party.WHITE: "X"},
    ):
        self.__SIZE_X = size_x
        self.__SIZE_Y = size_y
        self.state_markers_dict = markers_dict
        num_of_squares = size_x * size_y
        # in __state, states are stored row after row
        self.__state = [Party.NEUTRAL for i in range(0, num_of_squares)]

    def setValueAtCartesian(self, cart_pt: CartPt, new_val: Party) -> None:
        self.throwIfOutOfRange(cart_pt)
        self.__state[self.cartToLinearIdx(cart_pt)] = new_val

    def valueFromCartesian(self, cart_pt: CartPt) -> Party:
        self.throwIfOutOfRange(cart_pt)
        return self.__state[self.cartToLinearIdx(cart_pt)]

    def cartToLinearIdx(self, cart_pt: CartPt) -> int:
        return (self.numOfCols()) * cart_pt.x + cart_pt.y

    def setStateFromLinearList(self, input_list: list) -> None:
        """define __state with input row after row"""
        self.__state = input_list

    def numOfRows(self) -> int:
        return self.__SIZE_X

    def numOfCols(self) -> int:
        return self.__SIZE_Y

    def cartPtOutOfRange(self, cart_pt: CartPt) -> bool:
        max_x = self.numOfRows() - 1
        max_y = self.numOfCols() - 1
        x_out_of_range = not (0 <= cart_pt.x <= max_x)
        y_out_of_range = not (0 <= cart_pt.y <= max_y)
        return x_out_of_range or y_out_of_range

    def throwIfOutOfRange(self, cart_pt: CartPt) -> IndexError:
        """throw IndexError in case that indices in cart_pt point to coordinate outside of board limits"""
        if self.cartPtOutOfRange(cart_pt):
            raise IndexError(
                "CartPt yields Indices "
                + str(cart_pt)
                + " that are inappropriate in this context!"
            )

    def rowValsAsList(self, row_idx: int) -> list:
        if not (0 <= row_idx < self.numOfRows()):
            raise IndexError("row index out of range")
        res = []
        for icol in range(0, self.numOfCols()):
            current_pt = CartPt(row_idx, icol)
            res.append(self.valueFromCartesian(current_pt))
        return res

    def colValsAsList(self, col_idx: int) -> list:
        if not (0 <= col_idx < self.numOfCols()):
            raise IndexError("column index out of range")
        res = []
        for irow in range(0, self.numOfRows()):
            current_pt = CartPt(irow, col_idx)
            res.append(self.valueFromCartesian(current_pt))
        return res

    def maindiagValsAsList(self, diag_index: int) -> list:
        """return values of diagonal in main direction (top left to bottom right) as list.
        diag_index describes if main diagonal or which side diagonal.

        Args:
            diag_index (int): 0: main diagonal.
                        diag_index > 0: side diagnoal starting at top row
                        diag_index < 0: side diagonal starting at most left column

        Raises:
            IndexError: diag_index out of range

        Returns:
            list: values of main diagonal or if diag_index != 0 side diagonal in same direction
        """
        if not (-self.numOfRows() < diag_index < self.numOfCols()):
            raise IndexError(
                "diag index "
                + str(diag_index)
                + " out of range from "
                + str(-self.numOfRows() + 1)
                + " to "
                + str(self.numOfCols() - 1)
            )
        diag_index_positive = diag_index > 0
        top_left_pt_of_diag = (
            CartPt(0, diag_index) if diag_index_positive else CartPt(-diag_index, 0)
        )
        index_incr = 0
        res = []
        point_to_add = top_left_pt_of_diag
        while not self.cartPtOutOfRange(point_to_add):
            res.append(self.valueFromCartesian(point_to_add))
            index_incr += 1
            point_to_add = CartPt(
                top_left_pt_of_diag.x + index_incr, top_left_pt_of_diag.y + index_incr
            )
        return res

    def antidiagValsAsList(self, diag_index: int) -> list:
        """return values of diagonal in anti direction (top right to bottom left) as list.
        diag_index describes if anti diagonal or which side diagonal.

        Args:
            diag_index (int): 0: main diagonal.
                        diag_index < 0: side diagonal starting at top row
                        diag_index > 0: side diagonal starting at most right column

        Raises:
            IndexError: diag_index out of range

        Returns:
            list: values of main diagonal or if diag_index != 0 side diagonal in same direction
        """
        if not (-self.numOfCols() < diag_index < self.numOfRows()):
            raise IndexError(
                "diag index "
                + str(diag_index)
                + " out of range from "
                + str(self.numOfRows() - 1)
                + " to "
                + str(self.numOfCols() - 1)
            )
        max_col_index = self.numOfCols() - 1
        diag_index_positive = diag_index > 0
        top_right_pt_of_diag = (
            CartPt(diag_index, max_col_index)
            if diag_index_positive
            else CartPt(0, max_col_index - (-diag_index))
        )
        index_incr = 0
        point_to_add = top_right_pt_of_diag
        res = []
        while not self.cartPtOutOfRange(point_to_add):
            res.append(self.valueFromCartesian(point_to_add))
            index_incr += 1
            point_to_add = CartPt(
                top_right_pt_of_diag.x + index_incr, top_right_pt_of_diag.y - index_incr
            )
        return res

    @property
    def state(self):
        return self.__state

    @staticmethod
    def fromString(
        string: str,
        state_markers_dct={Party.NEUTRAL: "_", Party.WHITE: "X", Party.BLACK: "O"},
    ):
        markers_state_dct = {v: k for k, v in state_markers_dct.items()}
        list_of_lines = string.split("\n")
        list_of_lengths = [len(line) for line in list_of_lines]
        lines_same_length = all(l == list_of_lengths[0] for l in list_of_lengths)
        list_of_charlists = [list(str) for str in list_of_lines]
        if not lines_same_length:
            raise ValueError(
                "Board with assignment from string fixture: \
                        lines in input string are not equally long!"
            )
        list_of_party_lists = []

        for line in list_of_charlists:
            list_of_party_lists.append([markers_state_dct[char] for char in line])
        return Board.fromAssignmentLists(list_of_party_lists, state_markers_dct)

    @staticmethod
    def fromAssignmentLists(
        list_of_party_lists,
        state_markers_dct={Party.NEUTRAL: "_", Party.WHITE: "X", Party.BLACK: "O"},
    ):
        num_of_rows = len(list_of_party_lists)
        num_of_cols = len(list_of_party_lists[0])
        board = Board(num_of_rows, num_of_cols, state_markers_dct)
        for irow in range(0, num_of_rows):
            for icol in range(0, num_of_cols):
                current_pt = CartPt(irow, icol)
                current_val = list_of_party_lists[irow][icol]
                board.setValueAtCartesian(current_pt, current_val)
        return board

    def _getRowAssignmentsAsList(self, row_idx: int) -> list:
        if row_idx < 0 or row_idx > self.numOfRows() - 1:
            raise IndexError(
                "Line Index "
                + str(row_idx)
                + " is out of range. (num of rows = "
                + str(self.numOfRows())
                + ")"
            )
        return [
            self.valueFromCartesian(CartPt(row_idx, col_idx))
            for col_idx in range(0, self.numOfCols())
        ]

    def _rowToString(self, row_idx):
        if row_idx < 0 or row_idx > self.numOfRows() - 1:
            raise IndexError(
                "Line Index "
                + str(row_idx)
                + " is out of range. (num of rows = "
                + str(self.numOfRows())
                + ")"
            )
        charlist = [
            self.state_markers_dict[party]
            for party in self._getRowAssignmentsAsList(row_idx)
        ]
        return "".join(charlist)

    @staticmethod
    def _rowStringToFormatted(rowstring):
        res = ""
        if len(rowstring) <= 2:
            return rowstring
        first_char = rowstring[0]
        last_char = rowstring[-1]
        interior_string = rowstring[1:-1]
        print(interior_string)
        for i in range(len(interior_string) - 1, 0, -1):
            interior_string = interior_string[:i] + "|" + interior_string[i:]
        return first_char + "|" + interior_string + "|" + last_char

    def __str__(self):
        res = "Board:\n"
        row_idx_range = range(0, self.numOfRows())
        col_idx_range = range(0, self.numOfCols())
        col_index_row = 2 * " " + "".join([str(idx) for idx in col_idx_range])
        res += col_index_row + "\n"
        for irow in row_idx_range:
            res += str(irow) + "|"
            for icol in col_idx_range:
                char_to_add = self.state_markers_dict[
                    self.valueFromCartesian(CartPt(irow, icol))
                ]
                res += char_to_add
            if irow < self.numOfCols() - 1:
                res += "\n"
        res += 2 * "\n"
        res += (
            "Marker for "
            + Party.WHITE.name
            + ": "
            + self.state_markers_dict[Party.WHITE]
            + ";\t"
        )

        res += (
            "Marker for "
            + Party.BLACK.name
            + ": "
            + self.state_markers_dict[Party.BLACK]
        )

        return res
