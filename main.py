from game_execution import (
    GameExecution,
    GameStatus,
    createDefaultTicTacToeGameExecutionHumanPlayers,
)
from Party import Party
from board import Board
from human_player_tictactoe import HumanPlayerTicTacToe
from game_dynamics_tictactoe import GameDynamicsTicTacToe


def main():
    print("START")
    ge = createDefaultTicTacToeGameExecutionHumanPlayers()
    ge.executeGame()


if __name__ == "__main__":
    main()
