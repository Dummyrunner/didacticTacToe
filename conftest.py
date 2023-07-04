import pytest
from board import Board
from Party import Party
from game_dynamics_tictactoe import GameDynamicsTicTacToe


@pytest.fixture
def default_board3x3():
    state_markers_dct = {Party.NEUTRAL: "_", Party.WHITE: "X", Party.BLACK: "O"}
    res = Board(3, 3, state_markers_dct)
    return res


@pytest.fixture
def default_board3x4():
    state_markers_dct = {Party.NEUTRAL: "_", Party.WHITE: "X", Party.BLACK: "O"}
    res = Board(3, 4, state_markers_dct)
    return res


@pytest.fixture
def empty_states_default_board3x3():
    return 9 * [Party.NEUTRAL]


@pytest.fixture
def default_dynamics_tictactoe():
    board = Board(3, 3)
    rowsize_to_win = 3
    return GameDynamicsTicTacToe(board, rowsize_to_win)
