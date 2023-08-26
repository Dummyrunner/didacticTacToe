from board import BoardRectangular
from cartpt import CartPt
from Party import Party
from move import MoveTicTacToeGravity
import pytest
from game_dynamics import GameDynamicsTicTacToeGravity


def test_update_admissible_moves_gravity():
    line0 = "O___\n"
    line1 = "OO__\n"
    line2 = "OOX_"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    rowsize_to_win = 1000
    dynamics = GameDynamicsTicTacToeGravity(board, rowsize_to_win)

    assert type(dynamics.admissibleMoves()) == set
    actual_admissible_moves = dynamics.admissibleMoves()
    expected_admissible_moves_black = set(
        [MoveTicTacToeGravity(col, Party.BLACK) for col in [1, 2, 3]]
    )
    expected_admissible_moves_white = set(
        [MoveTicTacToeGravity(col, Party.WHITE) for col in [1, 2, 3]]
    )
    expected_admissible_moves = expected_admissible_moves_black.union(
        expected_admissible_moves_white
    )
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert set(actual_admissible_moves) == set(expected_admissible_moves)
    # check admissible moves for party
    assert dynamics.addmissibleMovesForParty(Party.WHITE) == set(
        expected_admissible_moves_white
    )
    assert dynamics.addmissibleMovesForParty(Party.BLACK) == set(
        expected_admissible_moves_black
    )
    # check, whether admissible move list is updated if board changes
    board.setValueAtCartesian(CartPt(0, 1), Party.WHITE)
    expected_admissible_moves.remove(MoveTicTacToeGravity(1, Party.WHITE))
    expected_admissible_moves.remove(MoveTicTacToeGravity(1, Party.BLACK))
    actual_admissible_moves = dynamics.admissibleMoves()
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == set(expected_admissible_moves)


def test_update_admissible_moves_party_gravity():
    line0 = "O___\n"
    line1 = "OO__\n"
    line2 = "OOX_"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    rowsize_to_win = 1000
    dynamics = GameDynamicsTicTacToeGravity(board, rowsize_to_win)

    expected_admissible_moves_black = set(
        [MoveTicTacToeGravity(col, Party.BLACK) for col in [1, 2, 3]]
    )
    expected_admissible_moves_white = set(
        [MoveTicTacToeGravity(col, Party.WHITE) for col in [1, 2, 3]]
    )
    actual_admissible_moves_white = dynamics.addmissibleMovesForParty(Party.WHITE)
    actual_admissible_moves_black = dynamics.addmissibleMovesForParty(Party.BLACK)
    assert type(actual_admissible_moves_black) == set
    assert type(actual_admissible_moves_white) == set
    assert len(actual_admissible_moves_white) == len(expected_admissible_moves_white)
    assert len(actual_admissible_moves_black) == len(expected_admissible_moves_black)
    assert actual_admissible_moves_white == set(expected_admissible_moves_white)
    assert actual_admissible_moves_black == set(expected_admissible_moves_black)


def test_dynamics_gravity_do_move_for_party():
    board = BoardRectangular(1, 2)
    dynamics = GameDynamicsTicTacToeGravity(board, 55)
    col_idx = 1
    col_idx_invalid = 2
    move = MoveTicTacToeGravity(col_idx, Party.BLACK)
    move_invalid = MoveTicTacToeGravity(col_idx_invalid, Party.BLACK)
    dynamics.doMoveForParty(Party.BLACK, move)
    floor_row_idx = board.numOfRows() - 1
    assert board.valueFromCartesian(CartPt(floor_row_idx, col_idx)) == Party.BLACK
    assert board.valueFromCartesian(CartPt(floor_row_idx, 0)) == Party.NEUTRAL
    with pytest.raises(ValueError):
        dynamics.doMoveForParty(Party.BLACK, move_invalid)
