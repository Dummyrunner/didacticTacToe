from player_tictactoe_ai import *
from board import BoardRectangular
from game_dynamics import GameDynamicsTicTacToe


def test_ai_build_decision_tree():
    board = BoardRectangular(1, 2)
    board.setValueAtCartesian(CartPt(0, 0), Party.WHITE)
    dynamics = GameDynamicsTicTacToe(board, 2)
    ai = AiTicTacToeMinimax(dynamics)
    actual_built_tree = ai._buildDecisionTree(board, Party.WHITE)
    num_of_nodes = len(actual_built_tree.bfsTraversal())
    assert num_of_nodes == 1
