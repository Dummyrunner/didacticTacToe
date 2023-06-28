from enum import Enum
from board import Board, CartPt, Party


class GameDynamicsTicTacToe:
    def __init__(self, board, rowsize_to_win):
        self.ROWSIZE_TO_WIN = rowsize_to_win
        self.board = board
        self.admissible_moves_set = set()
        self.updateAdmissibleMoves()

    def updateAdmissibleMoves(self):
        board = self.board
        num_of_rows = board.numOfRows()
        num_of_cols = board.numOfCols()
        self.admissible_moves_set = set()
        for irow in range(0, num_of_rows):
            for icol in range(0, num_of_cols):
                current_point = CartPt(irow, icol)
                if board.valueFromCartesian(current_point) == Party.NEUTRAL:
                    # admissible moves are for both parties the same. so neutral is to be considered a
                    # placeholder here
                    move_to_add_black = MoveTicTacToe(current_point, Party.BLACK)
                    move_to_add_white = MoveTicTacToe(current_point, Party.WHITE)
                    self.admissible_moves_set.add(move_to_add_white)
                    self.admissible_moves_set.add(move_to_add_black)

    def requestMoveFromPlayer(player):
        # TODO
        pass

    def doMoveOnBoard(self, player, move):
        party = player.party
        pt = move.cartpt_to_fill
        self.board.setValueAtCartesian(pt, party)

    def hasWonGame(party):
        # TODO
        pass


class HumanPlayerTicTacToe:
    def __init__(self, party, name=""):
        if name == "":
            self.name = self.generate_name
        else:
            self.name = name
        self.party = party

    def generate_name():
        ctr = 1
        while True:
            yield "Harald" + str(ctr)
            ctr += 1

    def chooseMove(self):
        pass


class MoveTicTacToe:
    """structure representing one move in tic tac toe

    Parameters:
            cartpt_to_fill (CartPt): cartesian target coordinates
            party (Party.*): Which party executes the move
            board (Board): Gameboard to perform the move on"""

    def __init__(self, cartpt_to_fill, party):
        self.cartpt_to_fill = cartpt_to_fill
        self.party = party

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
