from human_player_tictactoe import HumanPlayerTicTacToe
from Party import Party
from cartpt import CartPt


def test_init_human_player_tictactoe():
    hp = HumanPlayerTicTacToe(Party.BLACK, "Edgar Wasser")
    assert hp.name == "Edgar Wasser"
    assert hp.party == Party.BLACK


def test_init_human_player_tictactoe_no_name():
    hp_nameless = HumanPlayerTicTacToe(Party.WHITE)
    assert hp_nameless.party == Party.WHITE
    assert hp_nameless.name != ""


def test_human_player_tictactoe_parse_keyboard_input_to_move():
    hp = HumanPlayerTicTacToe(Party.WHITE, "Parserino")
    assert hp.parseKeyboardInputToMove("0,0") == CartPt(0, 0)
    assert hp.parseKeyboardInputToMove("2,3") == CartPt(2, 3)
