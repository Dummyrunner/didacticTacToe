from board import BoardRectangular
from Party import Party


def test_n_of_party_cohesive_seq_in_row():
    state_string = "O_O\nOOO\n_OO"
    board = BoardRectangular.fromString(state_string)
    assert board.maxLenCohesiveSeqInRowOfParty(0, Party.BLACK) == 1
    assert board.maxLenCohesiveSeqInRowOfParty(1, Party.BLACK) == 3
    assert board.maxLenCohesiveSeqInRowOfParty(2, Party.BLACK) == 2


def test_n_of_party_cohesive_seq_in_col():
    state_string = "OO_\n_OO\nOOO"
    board = BoardRectangular.fromString(state_string)
    assert board.maxLenCohesiveSeqInColOfParty(0, Party.BLACK) == 1
    assert board.maxLenCohesiveSeqInColOfParty(1, Party.BLACK) == 3
    assert board.maxLenCohesiveSeqInColOfParty(2, Party.BLACK) == 2
