from player_tictactoe_ai import AiTicTacToeMinimax, GameDynamicsTicTacToeWrapper
from board import BoardRectangular
from game_dynamics import GameDynamicsTicTacToe
from Party import Party
from cartpt import CartPt


# def test_ai_build_decision_tree():
#     board = BoardRectangular(1, 2)
#     board.setValueAtCartesian(CartPt(0, 0), Party.WHITE)
#     dynamics = GameDynamicsTicTacToe(board, 2)
#     ai = AiTicTacToeMinimax(dynamics)
#     actual_built_tree = ai._buildDecisionTree(board, Party.WHITE)
#     print("ACTUAL BUILD TREE:")
#     print(actual_built_tree)
#     # num_of_nodes = len(actual_built_tree.bfsTraversal())
#     # assert num_of_nodes == 1
#     assert 1 == 0
