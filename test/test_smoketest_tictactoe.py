from game_execution import GameExecution
from game_status import GameStatus
from board import BoardRectangular
from game_dynamics import GameDynamicsTicTacToe
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
    actual_status = smoketest_from_players(
        moves_white_white_wins, moves_black_white_wins
    )
    expected_status = GameStatus.WHITE_WINS
    assert actual_status == expected_status


moves_white_black_wins = ["0,0", "0,2", "2,2"]
moves_black_black_wins = ["1,1", "0,1", "2,1"]


def test_smoketest_black_wins():
    actual_status = smoketest_from_players(
        moves_white_black_wins, moves_black_black_wins
    )
    expected_status = GameStatus.BLACK_WINS
    assert actual_status == expected_status


moves_white_draw = ["0,0", "1,0", "2,1", "0,2", "1,2"]
moves_black_draw = ["0,1", "2,0", "1,1", "2,2"]


def test_smoketest_draw():
    actual_status = smoketest_from_players(moves_white_draw, moves_black_draw)
    expected_status = GameStatus.DRAW
    assert actual_status == expected_status


def smoketest_from_players(moves_white, moves_black):
    player_white = ScriptedPlayer(Party.WHITE, moves_white)
    player_black = ScriptedPlayer(Party.BLACK, moves_black)
    board = BoardRectangular(3, 3)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, player_white, player_black)
    return ge.executeGame()
