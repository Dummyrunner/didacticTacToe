from game_dynamics_tictactoe import GameDynamicsTicTacToe
from Party import Party
from enum import Enum


class GameExecution:
    def __init__(self, dynamics: GameDynamicsTicTacToe):
        self.__dynamics = dynamics
        self.__whos_turn = Party.WHITE
        self.winner = Party.NEUTRAL
        self.status = GameStatus.PREPARE

    def whosTurn(self) -> Party:
        return self.__whos_turn

    def setWhosTurn(self, party: Party) -> None:
        if party == Party.NEUTRAL:
            raise AttributeError("Here not a valid party option:" + str(party))
        if party.name not in Party.__members__ or not isinstance(party, Party):
            raise AttributeError("Not a valid party:" + str(party))
        self.__whos_turn = party

    def executeGame():
        # TODO
        pass


class GameStatus(Enum):
    PREPARE = 0
    RUNNING = 1
    FINISHED = 2
    FAILURE = 3
