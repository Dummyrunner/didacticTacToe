from board import Board
from cartpt import CartPt
from Party import Party
from move_tictactoe import MoveTicTacToe
from game_dynamics_tictactoe import GameDynamicsTicTacToe
import itertools


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


def test_admissible_moves_partially_occupied_black():
    dynamics = GameDynamicsTicTacToe(Board(1, 2), 2)
    board = dynamics.board
    board.setValueAtCartesian(CartPt(0, 0), Party.BLACK)
    expected_admissible_moves = [
        MoveTicTacToe(CartPt(0, 1), Party.BLACK),
    ]
    actual_admissible_moves = dynamics.addmissibleMovesForParty(Party.BLACK)
    assert len(actual_admissible_moves) == len(expected_admissible_moves)
    assert set(actual_admissible_moves) == set(expected_admissible_moves)
