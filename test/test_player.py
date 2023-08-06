from player_tictactoe import (
    HumanPlayerTicTacToe,
    BasePlayer,
    HumanPlayerTicTacToeGravity,
)
from Party import Party
from cartpt import CartPt
from move import MoveTicTacToe, MoveTicTacToeGravity
from io import StringIO
from pytest import raises
from types import MethodType


def test_player_input_topology_valid_bad_input():
    ip_string_senseless = "senselessInput"
    ip_string_too_many_comma = "1,2,3"
    pl = HumanPlayerTicTacToe(Party.BLACK)
    assert pl._inputTopologyValid(ip_string_senseless) == False
    assert pl._inputTopologyValid(ip_string_too_many_comma) == False


def test_input_topology_valid_good_input():
    ip_string1 = "1,2"
    ip_string2 = "33,99"
    pl = HumanPlayerTicTacToe(Party.BLACK)
    assert pl._inputTopologyValid(ip_string1) == True
    assert pl._inputTopologyValid(ip_string2) == True


def test_init_base_player_tictactoe():
    hp = BasePlayer(Party.BLACK, "Edgar Wasser")
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


def test_humanplayertictactoe_get_keyboard_input(monkeypatch, default_board3x3):
    hp = HumanPlayerTicTacToe(Party.WHITE, "keyboardtyper")
    hp.board = default_board3x3
    fake_keyboard_input = StringIO("1,2\n")
    monkeypatch.setattr("sys.stdin", fake_keyboard_input)
    assert hp.getMoveKeyBoardInput() == "1,2"


def test_humanplayertictactoegravity_get_keyboard_input(monkeypatch, default_board3x3):
    hp = HumanPlayerTicTacToeGravity(Party.WHITE, "keyboardtyper")
    hp.board = default_board3x3
    fake_keyboard_input = StringIO("1")
    monkeypatch.setattr("sys.stdin", fake_keyboard_input)
    assert hp.getMoveKeyBoardInput() == "1"


def test_humanplayer_choose_move_wronginput_til_exception(
    monkeypatch, default_board3x3
):
    def inputTopologyValid_FALSE(self, ip_string):
        return False

    hp = HumanPlayerTicTacToe(Party.WHITE, "movechooser1")
    hp.board = default_board3x3
    fake_keyboard_input_both_nonvalid = StringIO("1,2,3\n1,2,3\n")
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_both_nonvalid)
    hp._inputTopologyValid = MethodType(inputTopologyValid_FALSE, hp)
    with raises(ValueError):
        hp.chooseMove(2)


def test_humanplayer_choose_move_fallback_once(monkeypatch, default_board3x3):
    hp = HumanPlayerTicTacToe(Party.WHITE, "movechooser2")
    hp.board = default_board3x3
    fake_keyboard_input_first_nonvalid = StringIO("1,2,3\n1,2\n")
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_first_nonvalid)
    expected_move = MoveTicTacToe(CartPt(1, 2), Party.WHITE)
    assert hp.chooseMove(2) == expected_move


def test_player_get_name_from_keyboard(monkeypatch):
    fake_keyboard_input_first_name = StringIO("Hans Peter\n")
    hp = HumanPlayerTicTacToe(Party.WHITE)
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_first_name)
    assert hp._setNameFromKeyboard() == "Hans Peter"


def test_player_get_name_from_keyboard(monkeypatch):
    fake_keyboard_input_first_name = StringIO("\n")
    hp = HumanPlayerTicTacToe(Party.WHITE)
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_first_name)
    assert hp._setNameFromKeyboard() == "DefaultHumanPlayer"


def test_player_get_name_from_keyboard_fail(monkeypatch):
    fake_keyboard_input_first_name = StringIO("1Hans Peter\n")
    hp = HumanPlayerTicTacToe(Party.WHITE)
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_first_name)
    with raises(ValueError):
        assert hp._setNameFromKeyboard() == "Hans Peter"


def test_player_set_name():
    hp = HumanPlayerTicTacToe(Party.WHITE)
    hp.name = "oldnamenobodycares"
    hp.setName("Cookie")
    assert hp.name == "Cookie"


def test_player_set_name_via_keyboard(monkeypatch):
    fake_keyboard_input_first_name = StringIO("Knoedl\n")
    hp = HumanPlayerTicTacToe(Party.WHITE)
    monkeypatch.setattr("sys.stdin", fake_keyboard_input_first_name)
    hp.setNameFromKeyboard()
    assert hp.name == "Knoedl"


def test_input_topology_valid_gravity():
    pl = HumanPlayerTicTacToeGravity(Party.BLACK)
    assert pl._inputTopologyValid("0") == True
    assert pl._inputTopologyValid("1, 2") == False
    assert pl._inputTopologyValid("Hello") == False


def test_parse_keyboard_input_to_move_gravity():
    pl_black = HumanPlayerTicTacToeGravity(Party.BLACK)
    pl_white = HumanPlayerTicTacToeGravity(Party.WHITE)
    actual_move_black = pl_black.parseKeyboardInputToMove("3")
    actual_move_white = pl_white.parseKeyboardInputToMove("3")
    expected_move_black = MoveTicTacToeGravity(3, Party.BLACK)
    expected_move_white = MoveTicTacToeGravity(3, Party.WHITE)
    assert actual_move_black == expected_move_black
    assert actual_move_white == expected_move_white
    with raises(ValueError):
        pl_black.parseKeyboardInputToMove("Moin")
