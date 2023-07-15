from player_tictactoe import HumanPlayerTicTacToe
from Party import Party
from cartpt import CartPt
from board import Board
from move_tictactoe import MoveTicTacToe


def test_init_human_player_tictactoe():
    board = Board(1, 1)
    hp = HumanPlayerTicTacToe(Party.BLACK, "Edgar Wasser")
    assert hp.name == "Edgar Wasser"
    assert hp.party == Party.BLACK


def test_init_human_player_tictactoe_no_name():
    board = Board(1, 1)
    hp_nameless = HumanPlayerTicTacToe(Party.WHITE)
    assert hp_nameless.party == Party.WHITE
    assert hp_nameless.name == ""


def test_human_player_tictactoe_parse_keyboard_input_to_move():
    board = Board(1, 1)
    hp = HumanPlayerTicTacToe(Party.WHITE, "Parserino")
    assert hp.parseKeyboardInputToMove("0,0") == MoveTicTacToe(
        CartPt(0, 0), Party.WHITE
    )
    assert hp.parseKeyboardInputToMove("2,3") == MoveTicTacToe(
        CartPt(2, 3), Party.WHITE
    )
