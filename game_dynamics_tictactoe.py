from Party import Party
from cartpt import CartPt
from move_tictactoe import MoveTicTacToe


class GameDynamicsTicTacToe:
    def __init__(self, board, rowsize_to_win):
        self.ROWSIZE_TO_WIN = rowsize_to_win
        self.board = board
        self.admissible_moves_set = set()
        self.updateAdmissibleMoves()

    def updateAdmissibleMoves(self) -> None:
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

    def doMoveOnBoard(self, player, move) -> None:
        party = player.party
        pt = move.cartpt_to_fill
        self.board.setValueAtCartesian(pt, party)

    @staticmethod
    def cohesiveSeqInPartyList(party_list: list, party: Party) -> int:
        len_max_seq = 0
        current_seq_len = 0
        for x in party_list:
            if x.value == party.value:
                current_seq_len += 1
            else:
                len_max_seq = max(len_max_seq, current_seq_len)
                current_seq_len = 0
        len_max_seq = max(len_max_seq, current_seq_len)
        current_seq_len = 0
        return len_max_seq

    def cohesiveSeqInRowOfParty(self, row_idx: int, party: Party) -> int:
        rowvals_as_list = self.board.rowValsAsList(row_idx)
        return GameDynamicsTicTacToe.cohesiveSeqInPartyList(rowvals_as_list, party)

    def cohesiveSeqInColOfParty(self, col_idx: int, party: Party) -> int:
        colvals_as_list = self.board.colValsAsList(col_idx)
        return GameDynamicsTicTacToe.cohesiveSeqInPartyList(colvals_as_list, party)

    def hasWonGame(party):
        # TODO
        pass
