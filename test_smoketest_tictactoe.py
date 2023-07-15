from game_execution import (
    GameExecution,
    createDefaultTicTacToeGameExecutionHumanPlayers,
)
from human_player_tictactoe import HumanPlayerTicTacToe
from board import Board
from game_dynamics_tictactoe import GameDynamicsTicTacToe
from move_tictactoe import MoveTicTacToe
from cartpt import CartPt
from Party import Party

list_of_moves_white_white_wins = [
    MoveTicTacToe(CartPt(1, 1), Party.WHITE),
    MoveTicTacToe(CartPt(0, 0), Party.WHITE),
    MoveTicTacToe(CartPt(2, 0), Party.WHITE),
    MoveTicTacToe(CartPt(1, 0), Party.WHITE),
]

list_of_moves_black_white_wins = [
    MoveTicTacToe(CartPt(0, 1), Party.BLACK),
    MoveTicTacToe(CartPt(2, 2), Party.BLACK),
    MoveTicTacToe(CartPt(0, 2), Party.BLACK),
]


ge = createDefaultTicTacToeGameExecutionHumanPlayers()
