from Party import Party
from move import MoveTicTacToe, MoveTicTacToeGravity
from cartpt import CartPt
from player_tictactoe import BasePlayer
from .ai.tree.node import Node
from .ai.tree.tree import Tree


class AiPlayerTicTacToe(BasePlayer):
    def __init__(self, ai):
        self.ai = ai

    def chooseMove(self) -> MoveTicTacToe:
        raise NotImplementedError


class AiTicTacToeBase:
    def chooseMove(board, whos_turn: Party, party: Party):
        raise NotImplementedError
