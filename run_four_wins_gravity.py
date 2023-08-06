from game_execution_factories import createFourWinsGravityGameExecutionHumanPlayers


def main():
    ge = createFourWinsGravityGameExecutionHumanPlayers()
    ge.executeGame()


if __name__ == "__main__":
    main()
