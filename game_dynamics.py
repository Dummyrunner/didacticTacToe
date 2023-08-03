from Party import Party
from cartpt import CartPt
from move import MoveTicTacToe
from axis import Axis


class GameDynamicsBase:
    pass


class WinByCohesiveRow:
    def _hasPartyWonAtAxisByIndex(
        self, axis_idx: int, axis: Axis, party: Party
    ) -> bool:
        board = self.board
        if axis == Axis.ROW:
            return (
                board.maxLenCohesiveSeqInRowOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.COL:
            return (
                board.maxLenCohesiveSeqInColOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.MAINDIAG:
            return (
                board.maxLenCohesiveSeqInMaindiagOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.ANTIDIAG:
            return (
                board.maxLenCohesiveSeqInAntidiagOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        else:
            raise AttributeError(
                "Non-plausible Axis! Expected: Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG"
            )

    def _hasPartyWonAtAnyAxis(self, axis: Axis, party: Party) -> bool:
        board = self.board
        range_of_row_indices = range(0, board.numOfRows())
        range_of_col_indices = range(0, board.numOfCols())
        range_of_maindiag_indices = range(-(board.numOfRows() - 1), board.numOfCols())
        range_of_antidiag_indices = range(-board.numOfCols() + 1, board.numOfRows())
        if axis == Axis.ROW:
            enough_to_win = [
                board.maxLenCohesiveSeqInRowOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_row_indices
            ]
        elif axis == Axis.COL:
            enough_to_win = [
                board.maxLenCohesiveSeqInColOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_col_indices
            ]
        elif axis == Axis.MAINDIAG:
            enough_to_win = [
                board.maxLenCohesiveSeqInMaindiagOfParty(i, party)
                >= self.ROWSIZE_TO_WIN
                for i in range_of_maindiag_indices
            ]

        elif axis == Axis.ANTIDIAG:
            enough_to_win = [
                board.maxLenCohesiveSeqInAntidiagOfParty(i, party)
                >= self.ROWSIZE_TO_WIN
                for i in range_of_antidiag_indices
            ]
        else:
            raise AttributeError(
                "Non-plausible Axis! Expected: Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG"
            )
        return any(enough_to_win)

    def hasPartyWon(self, party: Party) -> bool:
        relevant_axes = [Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG]
        return any([self._hasPartyWonAtAnyAxis(axe, party) for axe in relevant_axes])

    def isDraw(self):
        someone_won = self.hasPartyWon(Party.BLACK) or self.hasPartyWon(Party.WHITE)
        return not someone_won and len(self.admissibleMoves()) == 0


class GameDynamicsTicTacToe(GameDynamicsBase, WinByCohesiveRow):
    def __init__(self, board, rowsize_to_win):
        self.ROWSIZE_TO_WIN = rowsize_to_win
        self.board = board
        self.__admissible_moves_set = set()

    def _updateAdmissibleMoves(self) -> None:
        board = self.board
        num_of_rows = board.numOfRows()
        num_of_cols = board.numOfCols()
        self.__admissible_moves_set = set()
        for irow in range(0, num_of_rows):
            for icol in range(0, num_of_cols):
                current_point = CartPt(irow, icol)
                if board.valueFromCartesian(current_point) == Party.NEUTRAL:
                    # admissible moves are for both parties the same. so neutral is to be considered a
                    # placeholder here
                    move_to_add_black = MoveTicTacToe(current_point, Party.BLACK)
                    move_to_add_white = MoveTicTacToe(current_point, Party.WHITE)
                    self.__admissible_moves_set.add(move_to_add_white)
                    self.__admissible_moves_set.add(move_to_add_black)

    def _doMoveForParty(self, party, move) -> None:
        pt = move.cartpt_to_fill
        if move in self.admissibleMoves():
            self.board.setValueAtCartesian(pt, party)
        else:
            raise ValueError("Move " + str(move) + " not admissible")

    def doMoveOnBoard(self, player, move) -> None:
        party = player.party
        self._doMoveForParty(party, move)

    def admissibleMoves(self):
        self._updateAdmissibleMoves()
        return self.__admissible_moves_set

    def addmissibleMovesForParty(self, party):
        all_admissible_moves = self.admissibleMoves()
        return [x for x in all_admissible_moves if x.party == party]


# class GameDynamicsTicTacToeGravity(GameDynamicsBase, WinByCohesiveRow):
#     def __init__(self, board, rowsize_to_win):
#         self.ROWSIZE_TO_WIN = rowsize_to_win
#         self.board = board
#         self.__admissible_moves_set = set()
