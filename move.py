from Party import Party


class MoveBase:
    """Base class for a move of a board game, executed by a specific party"""

    def __init__(self, party):
        self._party = party

    @property
    def party(self):
        return self._party

    def _partyStr(self):
        party_str = ""
        if self.party == Party.NEUTRAL:
            party_str = "neutral"
        elif self.party == Party.BLACK:
            party_str = "black"
        elif self.party == Party.WHITE:
            party_str = "white"
        else:
            raise AttributeError("Non-valid Party value passed to move object!")
        return party_str

    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError


class MoveTicTacToe(MoveBase):
    """Class representing one move in tic tac toe

    Parameters:
            cartpt_to_fill (CartPt): cartesian target coordinates
            party (Party.*): Which party executes the move
            board (Board): Gameboard to perform the move on"""

    def __init__(self, cartpt_to_fill, party):
        MoveBase.__init__(self, party)
        self.__cartpt_to_fill = cartpt_to_fill

    @property
    def cartpt_to_fill(self):
        return self.__cartpt_to_fill

    def __str__(self):
        string = "(move: " + str(self.cartpt_to_fill) + " " + self._partyStr() + " )"
        return string

    def __hash__(self):
        return hash((self.__cartpt_to_fill, self._party))

    def __eq__(self, other):
        if not isinstance(other, MoveTicTacToe):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return (
            self.__cartpt_to_fill == other.__cartpt_to_fill
            and self.party == other.party
        )


class MoveTicTacToeGravity(MoveBase):
    """Class representing one move in tic tac toe with gravity

    Parameters:
            target column index: integer index
            party (Party.*): Which party executes the move
            board (Board): Gameboard to perform the move on"""

    def __init__(self, target_column, party):
        MoveBase.__init__(self, party)
        if type(target_column) != int:
            raise AttributeError(
                "Column must be int, but is " + str(type(target_column))
            )
        self.__target_column = target_column

    @property
    def target_column(self):
        return self.__target_column

    def __str__(self):
        string = "(move: " + str(self.target_columnr) + " " + self._partyStr() + " )"
        return string

    def __hash__(self):
        return hash((self.__target_column, self._party))

    def __eq__(self, other):
        if not isinstance(other, MoveTicTacToeGravity):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return (
            self.__target_column == other.__target_column and self.party == other.party
        )
