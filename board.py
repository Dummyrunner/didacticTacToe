from enum import Enum


class Party(Enum):
    NEUTRAL = 0
    WHITE = 1
    BLACK = 2


class CartPt:
    """Cartesian point. holds two attributes x and y. x represents the row number,
    y the column number"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        string = "(" + str(self.x) + "," + str(self.y) + ")"
        return string

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        if not isinstance(other, CartPt):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


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
        markers_dict={Party.NEUTRAL: "_", Party.BLACK: "X", Party.WHITE: "O"},
    ):
        self.__SIZE_X = size_x
        self.__SIZE_Y = size_y
        self.state_markers_dict = markers_dict
        num_of_squares = size_x * size_y
        # in __state, states are stored row after row
        self.__state = [Party.NEUTRAL for i in range(0, num_of_squares)]

    def setValueAtCartesian(self, cart_pt, new_val):
        self.throwIfOutOfRange(cart_pt)
        row = cart_pt.x
        col = cart_pt.y
        self.__state[self.numOfRows() * row + col] = new_val

    def valueFromCartesian(self, cart_pt):
        self.throwIfOutOfRange(cart_pt)
        row = cart_pt.x
        col = cart_pt.y
        return self.__state[self.numOfRows() * row + col]

    def setStateFromLinearList(self, input_list):
        """define __state with input row after row"""
        self.__state = input_list

    def numOfRows(self):
        return self.__SIZE_X

    def numOfCols(self):
        return self.__SIZE_Y

    def cartPtOutOfRange(self, cart_pt):
        max_x = self.numOfRows() - 1
        max_y = self.numOfCols() - 1
        x_out_of_range = not (0 <= cart_pt.x <= max_x)
        y_out_of_range = not (0 <= cart_pt.y <= max_y)
        return x_out_of_range or y_out_of_range

    def throwIfOutOfRange(self, cart_pt):
        """throw IndexError in case that indices in cart_pt point to coordinate outside of board limits"""
        if self.cartPtOutOfRange(cart_pt):
            raise IndexError(
                "CartPt yields Indices that are inappropriate in this context!"
            )

    @property
    def state(self):
        return self.__state

    def __str__(self):
        res = ""
        for irow in range(0, self.numOfRows()):
            for icol in range(0, self.numOfCols()):
                char_to_add = self.state_markers_dict[
                    self.valueFromCartesian(CartPt(irow, icol))
                ]
                res += char_to_add
            if irow < self.numOfCols() - 1:
                res += "\n"
        return res
