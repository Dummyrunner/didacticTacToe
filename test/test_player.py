from player_tictactoe import HumanPlayerTicTacToe, BasePlayerTicTacToe
from Party import Party
from cartpt import CartPt
from board import Board
from move_tictactoe import MoveTicTacToe
from io import StringIO
from pytest import MonkeyPatch


def test_player_input_topology_valid_bad_input():
    ip_string_senseless = "senselessInput"
    ip_string_too_many_comma = "1,2,3"
    pl = BasePlayerTicTacToe(Party.BLACK)
    assert pl._inputTopologyValid(ip_string_senseless) == False
    assert pl._inputTopologyValid(ip_string_too_many_comma) == False


def test_input_topology_valid_good_input():
    ip_string1 = "1,2"
    ip_string2 = "33,99"
    pl = BasePlayerTicTacToe(Party.BLACK)
    assert pl._inputTopologyValid(ip_string1) == True
    assert pl._inputTopologyValid(ip_string2) == True


def test_init_base_player_tictactoe():
    hp = BasePlayerTicTacToe(Party.BLACK, "Edgar Wasser")
    assert hp.name == "Edgar Wasser"
    assert hp.party == Party.BLACK


def test_init_base_player_tictactoe_no_name():
    hp_nameless = HumanPlayerTicTacToe(Party.WHITE)
    assert hp_nameless.party == Party.WHITE
    assert hp_nameless.name == ""


def test_human_player_tictactoe_parse_keyboard_input_to_move():
    hp = HumanPlayerTicTacToe(Party.WHITE, "Parserino")
    assert hp.parseKeyboardInputToMove("0,0") == MoveTicTacToe(
        CartPt(0, 0), Party.WHITE
    )
    assert hp.parseKeyboardInputToMove("2,3") == MoveTicTacToe(
        CartPt(2, 3), Party.WHITE
    )


def test_humanplayer_get_keyboard_input(monkeypatch, default_board3x3):
    hp = HumanPlayerTicTacToe(Party.WHITE, "keyboardtyper")
    hp.board = default_board3x3
    keyboard_input = StringIO("1,2\n")
    monkeypatch.setattr("sys.stdin", keyboard_input)
    assert hp.getKeyBoardInput() == "1,2"
