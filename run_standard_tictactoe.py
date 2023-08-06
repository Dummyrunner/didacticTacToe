from game_execution_factories import createDefaultTicTacToeGameExecutionHumanPlayers


def main():
    ge = createDefaultTicTacToeGameExecutionHumanPlayers()
    ge.executeGame()


if __name__ == "__main__":
    main()
