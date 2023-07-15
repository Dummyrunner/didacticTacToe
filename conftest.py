import pytest
from board import Board
from Party import Party
from game_dynamics_tictactoe import GameDynamicsTicTacToe
from player_tictactoe import HumanPlayerTicTacToe


class ScriptedPlayer(HumanPlayerTicTacToe):
    def __init__(self, party: Party, inputlist: list, name="ScriptedPlayer"):
        super().__init__(party, name)
        self.__inputlist = iter(inputlist)

    def getKeyBoardInput(self) -> str:
        move_ip = next(self.__inputlist)
        print("set move from movelist: " + move_ip)
        return move_ip


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
