from Party import Party
from move import MoveTicTacToe, MoveTicTacToeGravity
from cartpt import CartPt
from player_tictactoe import BasePlayer
from ai.tree.node import Node
from ai.tree.tree import Tree
from game_dynamics import GameDynamicsBase, GameDynamicsTicTacToe
import copy as cp


class AiPlayerTicTacToe(BasePlayer):
    def __init__(self, party: Party, ai):
        super().__init__(party)
        self.ai = ai

    def chooseMove(self) -> MoveTicTacToe:
        return self.ai.chooseMove(self.board)


class AiBase:
    def __init__(self, dynamics: GameDynamicsBase):
        self._game_dynamics = dynamics
        self._whos_turn = 0
        self.gamestate_analysis = None

    @property
    def dynamics(self):
        return self._game_dynamics

    @property
    def whosTurn(self):
        return self._whos_turn

    def setWhosTurn(self, party: Party):
        self._whos_turn = party

    def chooseMove(self, board, whos_turn: Party, party: Party):
        return self._calculateBestMove(self)

    def _admissibleMoves(self, board, whos_turn):
        raise NotImplementedError

    def _calculateBestMove(self):
        raise NotImplementedError

    def _buildDecisionTreeFull(self, board, whos_turn):
        other_party = {Party.WHITE: Party.BLACK, Party.BLACK: Party.WHITE}
        game_state = {"board_state": board, "whos_turn": whos_turn, "evaluation": None}
        current_state_node = Node(game_state)
        # local_board = cp.deepcopy(board)
        # admissible_moves = self.gamestate_analysis._admissibleMoves()
        # for move in admissible_moves:
        #     # TODO
        #     resulting_dynamics = self.gamestate_analysis._resultingDynamics()
        #     resulting_whos_turn = other_party[game_state["whos_turn"]]

        #     # resulting_game_state = ...
        #     # current_state_node.addChild(resulting_game_state)
        #     break
        # # get admissible moves
        # # for each admissible move, calculate new state
        # # build subtrees recursively
        # raise NotImplementedError

    @staticmethod
    def boardAndWhosTurnToDict(board, whos_turn):
        return {"board_state": board, "whos_turn": whos_turn}


class AiTicTacToeMinimax(AiBase):
    def __init__(self, dynamics):
        super().__init__(dynamics)
        self.gamestate_analysis = GameDynamicsTicTacToeWrapper()


class GameDynamicsWrapper:
    def _admissibleMoves(self, board, whos_turn: Party):
        raise NotImplementedError

    def _resultingDynamics(self, board, move: MoveTicTacToe):
        raise NotImplementedError

    def _isTerminalState(self, board):
        raise NotImplementedError

    def _isTerminalStatePartyWins(self, board, party: Party):
        raise NotImplementedError


class GameDynamicsTicTacToeWrapper(GameDynamicsWrapper):
    def _admissibleMoves(self, board, whos_turn: Party):
        dynamics = GameDynamicsTicTacToe(board, 3)
        return dynamics.addmissibleMovesForParty(whos_turn)

    def _resultingDynamics(self, board, move: MoveTicTacToe):
        dynamics = GameDynamicsTicTacToe(board, 3)
        party = move.party
        dynamics.doMoveForParty(party, move)
        return cp.deepcopy(dynamics)

    def _isTerminalState(self, board):
        dynamics = GameDynamicsTicTacToe(board, 3)
        return dynamics.isTerminalState()

    def _isTerminalStatePartyWins(self, board, party: Party):
        dynamics = GameDynamicsTicTacToe(board, 3)
        return dynamics.isTerminalState() and dynamics.hasPartyWon(party)
