from game_dynamics_tictactoe import GameDynamicsTicTacToe
from Party import Party
from enum import Enum
from human_player_tictactoe import HumanPlayerTicTacToe


class GameExecution:
    def __init__(self, dynamics: GameDynamicsTicTacToe, player_white, player_black):
        self.__dynamics = dynamics
        self.__whos_turn = Party.WHITE
        self.winner = Party.NEUTRAL
        self.status = GameStatus.PREPARE
        self.player_white = player_white
        self.player_black = player_black
        self.party2player = {
            Party.BLACK: self.player_black,
            Party.WHITE: self.player_white,
        }

    def dynamics(self):
        return self.__dynamics

    def whosTurn(self) -> Party:
        return self.__whos_turn

    def setWhosTurn(self, party: Party) -> None:
        if party == Party.NEUTRAL:
            raise AttributeError("Here not a valid party option:" + str(party))
        if party.name not in Party.__members__ or not isinstance(party, Party):
            raise AttributeError("Not a valid party:" + str(party))
        self.__whos_turn = party

    def playerList(self):
        return [self.player_white, self.player_black]

    def currentPlayer(self):
        if self.__whos_turn == Party.NEUTRAL:
            raise ValueError("Try to get current player, but there is none!")
        return self.party2player[self.__whos_turn]

    def executeGame(self):
        self.status = GameStatus.RUNNING
        while self.status == GameStatus.RUNNING:
            dynamics = self.dynamics()
            board = dynamics.board
            print(board)
            print("---------------------")
            curr_pl = self.currentPlayer()
            curr_pl.updateBoard(self.dynamics().board)
            move = curr_pl.chooseMove()
            dynamics.doMoveOnBoard(curr_pl, move)
            print(board)
            self.setWhosTurn(self.otherParty(curr_pl.party))
            print("---------------------")
            if dynamics.hasPartyWon(curr_pl.party):
                self.status = GameStatus.FINISHED
                print("PLAYER " + curr_pl.name + " HAS WON!!")

    def otherParty(self, party):
        res = Party.NEUTRAL
        if party == Party.WHITE:
            return Party.BLACK
        elif party == Party.BLACK:
            return Party.WHITE
        else:
            raise ValueError(
                "other Party argument has to be Party.BLACK or Party.WHITE, but is  "
                + str(party)
            )


class GameStatus(Enum):
    PREPARE = 0
    RUNNING = 1
    FINISHED = 2
    FAILURE = 3
