from Party import Party


class MoveBase:
    """Base class for a move of a board game, executed by a specific party"""

    def __init__(self, party):
        self._party = party

    @property
    def party(self):
        return self._party


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
        party_str = ""
        if self.party == Party.NEUTRAL:
            party_str = "neutral"
        elif self.party == Party.BLACK:
            party_str = "black"
        else:
            party_str = "white"
        string = "(move: " + str(self.cartpt_to_fill) + " " + party_str + " )"
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
