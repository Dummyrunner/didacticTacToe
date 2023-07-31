from game_dynamics import GameDynamicsTicTacToe
from Party import Party
from game_status import GameStatus
from enum import Enum
from player_tictactoe import HumanPlayerTicTacToe
from move import MoveTicTacToe
from board import BoardRectangular
import str_utils as su


class GameExecution:
    def __init__(
        self,
        dynamics: GameDynamicsTicTacToe,
        player_white: HumanPlayerTicTacToe,
        player_black: HumanPlayerTicTacToe,
    ):
        self.status = GameStatus.PREPARE
        self.__dynamics = dynamics
        self.__whos_turn = Party.WHITE
        self.winner = Party.NEUTRAL
        self.player_white = player_white
        self.player_black = player_black
        if self.player_white.name == "" and self.player_black.name == "":
            namegen = self.generateName()
            self.player_white.name = next(namegen)
            self.player_black.name = next(namegen)
        self.party2player_dct = {
            Party.BLACK: self.player_black,
            Party.WHITE: self.player_white,
        }
        self.player2party_dct = {
            self.party2player_dct[key]: key for key in self.party2player_dct.keys()
        }
        self.winning_player2status_dct = {
            self.player_white: GameStatus.WHITE_WINS,
            self.player_black: GameStatus.BLACK_WINS,
        }

    def generateName(self):
        ctr = 1
        while True:
            yield "Harald" + str(ctr)
            ctr += 1

    def playerAssignmentCorrect(self) -> bool:
        if (
            self.player_white.party != Party.WHITE
            or self.player_black.party != Party.BLACK
        ):
            return False
        return True

    @property
    def dynamics(self):
        return self.__dynamics

    def whosTurn(self) -> Party:
        return self.__whos_turn

    def setWhosTurn(self, party: Party) -> None:
        if party == Party.NEUTRAL:
            raise AttributeError("Here not a valid party option:" + str(party))
        if not isinstance(party, Party):
            raise AttributeError("Not a valid party:" + str(party))
        self.__whos_turn = party

    def playerFromParty(self, party: Party) -> HumanPlayerTicTacToe:
        if party == Party.WHITE:
            return self.player_white
        if party == Party.BLACK:
            return self.player_black

    def changeTurnToNext(self) -> None:
        current = self.whosTurn()
        next = self.opponentParty(current)
        self.setWhosTurn(next)

    def opponentParty(self, party: Party) -> Party:
        if party == Party.NEUTRAL:
            raise AttributeError("Here not a valid party option:" + str(party))
        res = None
        if party == Party.BLACK:
            res = Party.WHITE
        if party == Party.WHITE:
            res = Party.BLACK
        return res

    def playerList(self):
        return [self.player_white, self.player_black]

    def currentPlayer(self):
        return self.party2player_dct[self.__whos_turn]

    def requestMoveFromPlayer(
        self, player: HumanPlayerTicTacToe, max_tries=2
    ) -> MoveTicTacToe:
        party = player.party
        dynamics = self.dynamics
        for num_of_tries in range(0, max_tries):
            move = player.chooseMove()
            if move in dynamics.addmissibleMovesForParty(party):
                return move
            num_of_tries += 1
            print(
                "Non-admissible move (" + str(num_of_tries) + "/" + str(max_tries) + ")"
            )
        raise ValueError(
            "Too many non-admissible moves from player "
            + player.name
            + " playing for party "
            + player.party.name
            + " entered."
        )

    def executeMove(self, player: HumanPlayerTicTacToe, move: MoveTicTacToe) -> None:
        self.dynamics.doMoveOnBoard(player, move)

    def publishBoardToPlayer(self, player: HumanPlayerTicTacToe) -> None:
        player.updateBoard(self.dynamics.board)

    def _introMessageString(self) -> str:
        headline = "WELCOME TO didacTICTACTOE!"
        welcome_msg = su.strInBox(headline, 40)
        res = welcome_msg + "\n"
        res += "Player for " + Party.WHITE.name + ": " + self.player_white.name + "\n"
        res += "Player for " + Party.BLACK.name + ": " + self.player_black.name + "\n"
        return res

    def executeGame(self) -> Enum:
        self.status = GameStatus.RUNNING
        self.status = self.evaluateGameState()
        print(self._introMessageString())
        while self.status == GameStatus.RUNNING:
            dynamics = self.dynamics
            board = dynamics.board
            print(board)
            print(25 * "-")
            curr_pl = self.currentPlayer()
            self.publishBoardToPlayer(curr_pl)
            move = self.requestMoveFromPlayer(curr_pl)
            self.executeMove(curr_pl, move)
            self.changeTurnToNext()
            print(25 * "-")
            self.status = self.evaluateGameState()
        print(board)
        self.displayResult()
        return self.status

    def displayResult(self):
        result_string = ""
        if self.status == GameStatus.DRAW:
            result_string = "DRAW!"
        elif self.status == GameStatus.BLACK_WINS:
            result_string = "BLACK WINS!"
        elif self.status == GameStatus.WHITE_WINS:
            result_string = "WHITE WINS!"
        elif self.status == GameStatus.FAILURE:
            result_string = "FAILURE!"
        print(su.strInBox(result_string, 40))

    def evaluateGameState(self) -> Enum:
        dynamics = self.dynamics
        player_white = self.player_white
        player_black = self.player_black
        if dynamics.isDraw():
            return GameStatus.DRAW
        if dynamics.hasPartyWon(self.player2party_dct[player_white]):
            return self.winning_player2status_dct[player_white]
        if dynamics.hasPartyWon(self.player2party_dct[player_black]):
            return self.winning_player2status_dct[player_black]
        return GameStatus.RUNNING

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
    board = BoardRectangular(9, 9)
    rowsize_to_win = 5
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    return GameExecution(dyn, pwhite, pblack)
