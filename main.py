from game_execution import GameExecution, GameStatus
from Party import Party
from board import Board
from human_player_tictactoe import HumanPlayerTicTacToe
from game_dynamics_tictactoe import GameDynamicsTicTacToe


def main():
    print("START")
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    board = Board(3, 3)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)

    ge = GameExecution(dyn, pwhite, pblack)
    ge.executeGame()


if __name__ == "__main__":
    main()
