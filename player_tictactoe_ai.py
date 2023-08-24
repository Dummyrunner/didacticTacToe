from Party import Party
from move import MoveTicTacToe, MoveTicTacToeGravity
from cartpt import CartPt
from player_tictactoe import BasePlayer
from .ai.tree.node import Node
from .ai.tree.tree import Tree
from game_dynamics import GameDynamicsBase
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

    def _calculateBestMove(self):
        raise NotImplementedError

    def _buildDecisionTree(self, board, whos_turn):
        game_state = {"board_state": board, "whos_turn": whos_turn}
        current_state_node = Node(game_state)
        local_board = cp.deepcopy(board)
        admissible_moves = self.dynamics.admissibleMovesForParty(
            game_state["whos_turn"]
        )
        for move in admissible_moves:
            # TODO
            # resulting_game_state = ...
            # current_state_node.addChild(resulting_game_state)
            break
        # get admissible moves
        # for each admissible move, calculate new state
        # build subtrees recursively
        raise NotImplementedError

    @staticmethod
    def boardAndWhosTurnToDict(board, whos_turn):
        return {"board_state": board, "whos_turn": whos_turn}
