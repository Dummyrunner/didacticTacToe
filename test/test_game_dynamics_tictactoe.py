import pytest
from board import BoardRectangular
from cartpt import CartPt
from Party import Party
from move import MoveTicTacToe

from axis import Axis
from game_dynamics import GameDynamicsTicTacToe, GameDynamicsTicTacToeGravity
import itertools
from player_tictactoe import HumanPlayerTicTacToe


def test_do_move_on_board(default_dynamics_tictactoe):
    dynamics = default_dynamics_tictactoe
    board = dynamics.board
    center_square = CartPt(1, 1)
    corner_square = CartPt(2, 2)
    player_black = HumanPlayerTicTacToe(Party.BLACK)
    player_white = HumanPlayerTicTacToe(Party.WHITE)
    move_black_in_center = MoveTicTacToe(center_square, Party.BLACK)
    move_white_on_corner = MoveTicTacToe(corner_square, Party.WHITE)

    dynamics.doMoveOnBoard(player_black, move_black_in_center)
    dynamics.doMoveOnBoard(player_white, move_white_on_corner)

    assert board.valueFromCartesian(center_square) == Party.BLACK
    assert board.valueFromCartesian(corner_square) == Party.WHITE


def test_do_move_on_board_nonadmissible(default_dynamics_tictactoe):
    hp = HumanPlayerTicTacToe(Party.WHITE)
    dynamics = default_dynamics_tictactoe
    center_square = CartPt(1, 1)
    board = dynamics.board
    board.setValueAtCartesian(center_square, Party.WHITE)
    move = MoveTicTacToe(center_square, Party.BLACK)
    with pytest.raises(ValueError):
        dynamics.doMoveOnBoard(hp, move)


def test_has_party_won_at_any_axis_antidiags():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics._hasPartyWonAtAnyAxis(Axis.ROW, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAnyAxis(Axis.ROW, Party.WHITE) == False

    assert dynamics._hasPartyWonAtAnyAxis(Axis.COL, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAnyAxis(Axis.COL, Party.WHITE) == False

    assert dynamics._hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics._hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.WHITE) == False

    assert dynamics._hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.BLACK) == True
    assert dynamics._hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.WHITE) == False
    with pytest.raises(AttributeError):
        dynamics._hasPartyWonAtAnyAxis(Axis.BLUBBER, Party.WHITE)
    with pytest.raises(AttributeError):
        dynamics._hasPartyWonAtAnyAxis("KNOEDL", Party.WHITE)


def test_has_party_won_at_any_axis_antidiags_byindex_fails():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    with pytest.raises(AttributeError):
        dynamics._hasPartyWonAtAxisByIndex(0, Axis.BLUBBER, Party.WHITE)


def test_has_party_won_game():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWon(Party.BLACK) == True
    assert dynamics.hasPartyWon(Party.WHITE) == False

    line0 = "OXOX\n"
    line1 = "X_OX\n"
    line2 = "_OXX"
    state_string = line0 + line1 + line2
    board2 = BoardRectangular.fromString(state_string)
    rowsize_to_win = 3
    dynamics2 = GameDynamicsTicTacToe(board2, rowsize_to_win)

    assert dynamics2.hasPartyWon(Party.BLACK) == False
    assert dynamics2.hasPartyWon(Party.WHITE) == True


def test_admissible_moves_emptyboard(default_board3x4):
    board = default_board3x4
    dynamics = GameDynamicsTicTacToe(board, 3)
    row_idx_range = range(0, dynamics.board.numOfRows())
    col_idx_range = range(0, dynamics.board.numOfCols())
    cartesian_index_set = list(itertools.product(row_idx_range, col_idx_range))
    free_cartpt = [CartPt(*pt) for pt in cartesian_index_set]
    expected_admissible_moves = set()
    expected_admissible_move_pairs = [
        [MoveTicTacToe(pt, Party.BLACK), MoveTicTacToe(pt, Party.WHITE)]
        for pt in free_cartpt
    ]
    for mv_pair in expected_admissible_move_pairs:
        expected_admissible_moves.add(mv_pair[0])
        expected_admissible_moves.add(mv_pair[1])
    actual_admissible_moves = dynamics.admissibleMoves()

    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == expected_admissible_moves


def test_admissible_moves_emptyboard_party(default_board3x4):
    board = default_board3x4
    dynamics = GameDynamicsTicTacToe(board, 3)
    row_idx_range = range(0, dynamics.board.numOfRows())
    col_idx_range = range(0, dynamics.board.numOfCols())
    cartesian_index_set = list(itertools.product(row_idx_range, col_idx_range))
    free_cartpt = [CartPt(*pt) for pt in cartesian_index_set]
    actual_admissible_moves_black = set(dynamics.addmissibleMovesForParty(Party.BLACK))
    expected_admissible_moves_black = set(
        [MoveTicTacToe(pt, Party.BLACK) for pt in free_cartpt]
    )
    expected_admissible_moves_white = set(
        [MoveTicTacToe(pt, Party.WHITE) for pt in free_cartpt]
    )
    actual_admissible_moves_white = set(dynamics.addmissibleMovesForParty(Party.WHITE))
    assert len(actual_admissible_moves_white) == len(expected_admissible_moves_white)
    assert (
        actual_admissible_moves_white.difference(expected_admissible_moves_white)
        == set()
    )
    assert len(actual_admissible_moves_black) == len(expected_admissible_moves_black)
    assert (
        actual_admissible_moves_black.difference(expected_admissible_moves_black)
        == set()
    )


def test_admissible_moves_fullboard():
    dynamics = GameDynamicsTicTacToe(BoardRectangular(1, 2), 2)
    board = dynamics.board
    board.setStateFromLinearList(2 * [Party.BLACK])
    expected_admissible_moves = set()
    actual_admissible_moves = dynamics.admissibleMoves()
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == expected_admissible_moves


def test_admissible_moves_partially_occupied_miinimal():
    dynamics = GameDynamicsTicTacToe(BoardRectangular(1, 2), 2)
    board = dynamics.board
    board.setValueAtCartesian(CartPt(0, 0), Party.BLACK)
    expected_admissible_moves = set(
        [
            MoveTicTacToe(CartPt(0, 1), Party.BLACK),
            MoveTicTacToe(CartPt(0, 1), Party.WHITE),
        ]
    )
    actual_admissible_moves = dynamics.admissibleMoves()
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == expected_admissible_moves


def test_admissible_moves_partially_occupied_black():
    dynamics = GameDynamicsTicTacToe(BoardRectangular(1, 2), 2)
    board = dynamics.board
    board.setValueAtCartesian(CartPt(0, 0), Party.BLACK)
    expected_admissible_moves = [
        MoveTicTacToe(CartPt(0, 1), Party.BLACK),
    ]
    actual_admissible_moves = dynamics.addmissibleMovesForParty(Party.BLACK)
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert set(actual_admissible_moves) == set(expected_admissible_moves)


def test_is_draw_positive():
    line0 = "XOX\n"
    line1 = "OXO\n"
    line2 = "OXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    dynamics = GameDynamicsTicTacToe(board, 3)
    assert dynamics.isDraw() == True


def test_is_draw_negative_someone_won():
    line0 = "XOX\n"
    line1 = "OXO\n"
    line2 = "OOX"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    dynamics = GameDynamicsTicTacToe(board, 3)
    assert dynamics.isDraw() == False


def test_is_draw_negative_moves_left():
    line0 = "XOX\n"
    line1 = "O_O\n"
    line2 = "OXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)
    dynamics = GameDynamicsTicTacToe(board, 3)
    assert dynamics.isDraw() == False
