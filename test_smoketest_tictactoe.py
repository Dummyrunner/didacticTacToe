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

list_of_moves_white_white_wins = [
    "1,1",
    "0,0",
    "2,0",
    "1,0",
]

list_of_moves_black_white_wins = [
    "0,1",
    "2,2",
    "0,2",
]

pwhite = ScriptedPlayer(Party.WHITE, list_of_moves_white_white_wins)
pblack = ScriptedPlayer(Party.BLACK, list_of_moves_black_white_wins)
board = Board(3, 3)
rowsize_to_win = 3
dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
ge = GameExecution(dyn, pwhite, pblack)
ge.executeGame()
expected_status = GameStatus.WHITE_WINS
actual_status = ge.status
assert actual_status == expected_status
