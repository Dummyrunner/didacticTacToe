from cartpt import CartPt


class MoveTicTacToe:
    """structure representing one move in tic tac toe

    Parameters:
            cartpt_to_fill (CartPt): cartesian target coordinates
            party (Party.*): Which party executes the move
            board (Board): Gameboard to perform the move on"""

    def __init__(self, cartpt_to_fill, party):
        self.__cartpt_to_fill = cartpt_to_fill
        self.__party = party

    @property
    def cartpt_to_fill(self):
        return self.__cartpt_to_fill

    @property
    def party(self):
        return self.__party

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
        return hash((self.__cartpt_to_fill, self.__party))

    def __eq__(self, other):
        if not isinstance(other, MoveTicTacToe):
            #         don't attempt to compare against unrelated types
            return NotImplemented
        return (
            self.__cartpt_to_fill == other.__cartpt_to_fill
            and self.party == other.party
        )
