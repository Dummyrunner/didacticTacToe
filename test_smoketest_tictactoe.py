from game_execution import (
    GameExecution,
    GameStatus,
)
from player_tictactoe import HumanPlayerTicTacToe
from board import Board
from game_dynamics_tictactoe import GameDynamicsTicTacToe
from move_tictactoe import MoveTicTacToe
from cartpt import CartPt
from Party import Party
from conftest import ScriptedPlayer

moves_white_white_wins = [
    "1,1",
    "0,0",
    "2,0",
    "1,0",
]

moves_black_white_wins = [
    "0,1",
    "2,2",
    "0,2",
]


def test_smoketest_white_wins():
    pwhite = ScriptedPlayer(Party.WHITE, moves_white_white_wins)
    pblack = ScriptedPlayer(Party.BLACK, moves_black_white_wins)
    actual_status = smoketest_from_players(pwhite, pblack)
    expected_status = GameStatus.WHITE_WINS
    assert actual_status == expected_status


def smoketest_from_players(player_white, player_black):
    board = Board(3, 3)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, player_white, player_black)
    ge.executeGame()
    actual_status = ge.status
    return actual_status
