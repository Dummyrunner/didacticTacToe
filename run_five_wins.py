from game_execution_factories import createFiveWinsGameExecutionHumanPlayers


def main():
    ge = createFiveWinsGameExecutionHumanPlayers()
    ge.executeGame()


if __name__ == "__main__":
    main()
