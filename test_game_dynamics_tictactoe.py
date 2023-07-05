import pytest
from enum import Enum
from board import Board
from cartpt import CartPt
from Party import Party
from move_tictactoe import MoveTicTacToe

from axis import Axis
from game_dynamics_tictactoe import GameDynamicsTicTacToe
import itertools
from human_player_tictactoe import HumanPlayerTicTacToe


def test_doMoveOnBoard(default_dynamics_tictactoe):
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


def test_move_tictactoe_equality_overload():
    pt1 = CartPt(0, 0)
    pt2 = CartPt(0, 1)
    move1 = MoveTicTacToe(pt1, Party.BLACK)
    move2 = MoveTicTacToe(pt1, Party.WHITE)
    move3 = MoveTicTacToe(pt1, Party.WHITE)
    assert move2 == move3
    assert move1 != move2
    assert move1 != move3
    with pytest.raises(AssertionError):
        assert move1 == 333


def test_has_party_won_at_any_axis_antidiags():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWonAtAnyAxis(Axis.ROW, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.ROW, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.COL, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.COL, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.BLACK) == False
    assert dynamics.hasPartyWonAtAnyAxis(Axis.MAINDIAG, Party.WHITE) == False

    assert dynamics.hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.BLACK) == True
    assert dynamics.hasPartyWonAtAnyAxis(Axis.ANTIDIAG, Party.WHITE) == False


def test_has_party_won_game():
    line0 = "OXO_\n"
    line1 = "OOO_\n"
    line2 = "OOXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)
    rowsize_to_win = 3
    dynamics = GameDynamicsTicTacToe(board, rowsize_to_win)

    assert dynamics.hasPartyWon(Party.BLACK) == True
    assert dynamics.hasPartyWon(Party.WHITE) == False

    line0 = "OXOX\n"
    line1 = "X_OX\n"
    line2 = "_OXX"
    state_string = line0 + line1 + line2
    board2 = Board.fromString(state_string)
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
    expected_admissible_moves_raw = [
        [MoveTicTacToe(pt, Party.BLACK), MoveTicTacToe(pt, Party.WHITE)]
        for pt in free_cartpt
    ]
    for mv_pair in expected_admissible_moves_raw:
        expected_admissible_moves.add(mv_pair[0])
        expected_admissible_moves.add(mv_pair[1])
    actual_admissible_moves = dynamics.admissibleMoves()

    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == expected_admissible_moves


def test_admissible_moves_fullboard():
    dynamics = GameDynamicsTicTacToe(Board(1, 2), 2)
    board = dynamics.board
    board.setStateFromLinearList(2 * [Party.BLACK])
    expected_admissible_moves = set()
    actual_admissible_moves = dynamics.admissibleMoves()
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert actual_admissible_moves == expected_admissible_moves


def test_admissible_moves_partially_occupied_miinimal():
    dynamics = GameDynamicsTicTacToe(Board(1, 2), 2)
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
