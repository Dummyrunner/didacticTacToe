from Party import Party
from cartpt import CartPt
from move_tictactoe import MoveTicTacToe
from enum import Enum
from axis import Axis
from board import Board


class GameDynamicsTicTacToe:
    def __init__(self, board, rowsize_to_win):
        self.ROWSIZE_TO_WIN = rowsize_to_win
        self.board = board
        self.__admissible_moves_set = set()
        self.updateAdmissibleMoves()

    def updateAdmissibleMoves(self) -> None:
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

    def admissibleMoves(self):
        self.updateAdmissibleMoves()
        return self.__admissible_moves_set

    def addmissibleMovesForParty(self, party):
        all_admissible_moves = self.admissibleMoves()
        return [x for x in all_admissible_moves if x.party == party]

    def requestMoveFromPlayer(player):
        # TODO
        pass

    def doMoveOnBoard(self, player, move) -> None:
        # TODO catch non admissible move
        party = player.party
        pt = move.cartpt_to_fill
        self.board.setValueAtCartesian(pt, party)

    @staticmethod
    def maxLenCohesiveSeqInPartyList(party_list: list, party_of_interest: Party) -> int:
        len_max_seq = 0
        current_seq_len = 0
        for party in party_list:
            if party.value == party_of_interest.value:
                current_seq_len += 1
            else:
                len_max_seq = max(len_max_seq, current_seq_len)
                current_seq_len = 0
        len_max_seq = max(len_max_seq, current_seq_len)
        current_seq_len = 0
        return len_max_seq

    def maxLenCohesiveSeqInRowOfParty(self, row_idx: int, party: Party) -> int:
        rowvals_as_list = self.board.rowValsAsList(row_idx)
        return GameDynamicsTicTacToe.maxLenCohesiveSeqInPartyList(
            rowvals_as_list, party
        )

    def maxLenCohesiveSeqInColOfParty(self, col_idx: int, party: Party) -> int:
        colvals_as_list = self.board.colValsAsList(col_idx)
        return GameDynamicsTicTacToe.maxLenCohesiveSeqInPartyList(
            colvals_as_list, party
        )

    def maxLenCohesiveSeqInMaindiagOfParty(self, diag_idx: int, party: Party) -> int:
        maindiagvals_as_list = self.board.maindiagValsAsList(diag_idx)
        return GameDynamicsTicTacToe.maxLenCohesiveSeqInPartyList(
            maindiagvals_as_list, party
        )

    def maxLenCohesiveSeqInAntidiagOfParty(self, diag_idx: int, party: Party) -> int:
        antidiagvals_as_list = self.board.antidiagValsAsList(diag_idx)
        return GameDynamicsTicTacToe.maxLenCohesiveSeqInPartyList(
            antidiagvals_as_list, party
        )

    def hasPartyWonAtAxisByIndex(self, axis_idx: int, axis: Axis, party: Party) -> bool:
        if axis == Axis.ROW:
            return (
                self.maxLenCohesiveSeqInRowOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.COL:
            return (
                self.maxLenCohesiveSeqInColOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.MAINDIAG:
            return (
                self.maxLenCohesiveSeqInMaindiagOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        elif axis == Axis.ANTIDIAG:
            return (
                self.maxLenCohesiveSeqInAntidiagOfParty(axis_idx, party)
                >= self.ROWSIZE_TO_WIN
            )
        else:
            raise AttributeError(
                "Non-plausible Axis! Expected: Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG"
            )

    def hasPartyWonAtAnyAxis(self, axis: Axis, party: Party) -> bool:
        #     # TODO
        board = self.board
        range_of_row_indices = range(0, board.numOfRows())
        range_of_col_indices = range(0, board.numOfCols())
        range_of_maindiag_indices = range(-(board.numOfRows() - 1), board.numOfCols())
        range_of_antidiag_indices = range(-board.numOfCols() + 1, board.numOfRows())
        if axis == Axis.ROW:
            enough_to_win = [
                self.maxLenCohesiveSeqInRowOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_row_indices
            ]
        elif axis == Axis.COL:
            enough_to_win = [
                self.maxLenCohesiveSeqInColOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_col_indices
            ]
        elif axis == Axis.MAINDIAG:
            enough_to_win = [
                self.maxLenCohesiveSeqInMaindiagOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_maindiag_indices
            ]

        elif axis == Axis.ANTIDIAG:
            enough_to_win = [
                self.maxLenCohesiveSeqInAntidiagOfParty(i, party) >= self.ROWSIZE_TO_WIN
                for i in range_of_antidiag_indices
            ]
        else:
            raise AttributeError(
                "Non-plausible Axis! Expected: Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG"
            )
        return any(enough_to_win)

    def hasPartyWon(self, party: Party) -> bool:
        relevant_axes = [Axis.ROW, Axis.COL, Axis.MAINDIAG, Axis.ANTIDIAG]
        return any([self.hasPartyWonAtAnyAxis(axe, party) for axe in relevant_axes])

    def isDraw(self):
        # TODO Test!
        self.updateAdmissibleMoves()
        someone_won = self.hasPartyWon(Party.BLACK) or self.hasPartyWon(Party.WHITE)
        return not someone_won and self.admissibleMoves == set()
