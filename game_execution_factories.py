from game_dynamics import GameDynamicsTicTacToe, GameDynamicsTicTacToeGravity
from Party import Party
from player_tictactoe import HumanPlayerTicTacToe, HumanPlayerTicTacToeGravity
from board import BoardRectangular
from game_execution import GameExecution


def createDefaultTicTacToeGameExecutionHumanPlayers() -> GameExecution:
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    pwhite.setNameFromKeyboard()
    pblack.setNameFromKeyboard()
    board = BoardRectangular(3, 3)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    return GameExecution(dyn, pwhite, pblack)


def createFiveWinsGameExecutionHumanPlayers() -> GameExecution:
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    pwhite.setNameFromKeyboard()
    pblack.setNameFromKeyboard()
    board = BoardRectangular(15, 15)
    rowsize_to_win = 5
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    return GameExecution(dyn, pwhite, pblack)


def createFourWinsGravityGameExecutionHumanPlayers() -> GameExecution:
    pwhite = HumanPlayerTicTacToeGravity(Party.WHITE)
    pblack = HumanPlayerTicTacToeGravity(Party.BLACK)
    pwhite.setNameFromKeyboard()
    pblack.setNameFromKeyboard()
    board = BoardRectangular(7, 6)
    rowsize_to_win = 4
    dyn = GameDynamicsTicTacToeGravity(board, rowsize_to_win)
    return GameExecution(dyn, pwhite, pblack)
