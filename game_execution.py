from game_dynamics_tictactoe import GameDynamicsTicTacToe
from Party import Party
from enum import Enum
from player_tictactoe import HumanPlayerTicTacToe
from move_tictactoe import MoveTicTacToe
from board import Board


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
        self.party2player_dct = {
            Party.BLACK: self.player_black,
            Party.WHITE: self.player_white,
        }
        self.player2party_dct = {
            self.party2player_dct[key]: key for key in self.party2player_dct.keys()
        }

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
        if party.name not in Party.__members__ or not isinstance(party, Party):
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
        if self.__whos_turn == Party.NEUTRAL:
            raise ValueError("Try to get current player, but there is none!")
        return self.party2player_dct[self.__whos_turn]

    def _inputTopologyValid(ip_string: str, split_char=",") -> bool:
        """True, if input string ip_string contanins two integer values separated by one comma"""
        how_many_commas = ip_string.count(split_char)
        if how_many_commas != 1:
            return False
        x, y = ip_string.split(split_char)
        return x.isdigit() and y.isdigit()

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

    def executeGame(self):
        self.status = GameStatus.RUNNING
        while self.status == GameStatus.RUNNING:
            dynamics = self.dynamics
            board = dynamics.board
            print(board)
            print("---------------------")
            curr_pl = self.currentPlayer()
            self.publishBoardToPlayer(curr_pl)
            move = self.requestMoveFromPlayer(curr_pl)
            self.executeMove(curr_pl, move)
            print(board)
            self.changeTurnToNext()
            print("---------------------")
            dynamics.updateAdmissibleMoves()
            if dynamics.hasPartyWon(curr_pl.party):
                self.status = GameStatus.FINISHED
                print(
                    "PLAYER "
                    + curr_pl.name
                    + " ("
                    + curr_pl.party.name
                    + ") "
                    + " HAS WON!!"
                )  #
            elif dynamics.isDraw():
                print("DRAW!!\n")  #
                self.status = GameStatus.FINISHED

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
    board = Board(3, 3)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    return GameExecution(dyn, pwhite, pblack)


class GameStatus(Enum):
    PREPARE = 0
    RUNNING = 1
    FINISHED = 2
    FAILURE = 3
