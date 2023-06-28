from enum import Enum
from board import Board, CartPt, Party


class GameDynamicsTicTacToe:
    def __init__(self, board, rowsize_to_win):
        self.ROWSIZE_TO_WIN = rowsize_to_win
        self.board = board
        self.admissible_moves_list = []
        self.updateAdmissibleMoves()

    def updateAdmissibleMoves(self):
        board = self.board
        num_of_rows = board.numOfRows()
        num_of_cols = board.numOfCols()
        self.admissible_moves_list.clear()
        for irow in range(0, num_of_rows):
            for icol in range(0, num_of_cols):
                current_point = CartPt(irow, icol)
                print("current point:  " + str(current_point))
                if board.valueFromCartesian(current_point) == Party.NEUTRAL:
                    # admissible moves are for both parties the same. so neutral is to be considered a
                    # placeholder here
                    move_to_add = MoveTicTacToe(current_point, Party.NEUTRAL)
                    self.admissible_moves_list.append(move_to_add)

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
