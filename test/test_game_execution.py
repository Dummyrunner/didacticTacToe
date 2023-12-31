from game_execution import *
from game_execution_factories import (
    createDefaultTicTacToeGameExecutionHumanPlayers,
    createFiveWinsGameExecutionHumanPlayers,
    createFourWinsGravityGameExecutionHumanPlayers,
)
from Party import Party
import pytest
from player_tictactoe import HumanPlayerTicTacToe
from board import BoardRectangular
from game_dynamics import GameDynamicsTicTacToe
from cartpt import CartPt
from types import MethodType
from move import MoveTicTacToe
from io import StringIO
from game_status import GameStatus


def test_game_execution_init(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.whosTurn() == Party.WHITE
    ge.setWhosTurn(Party.BLACK)
    assert ge.whosTurn() == Party.BLACK
    assert ge.winner == Party.NEUTRAL
    assert ge.status == GameStatus.PREPARE


def test_game_execution_init_fail(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    with pytest.raises(AttributeError):
        ge.setWhosTurn(Party.NEUTRAL)
    with pytest.raises(AttributeError):
        ge.setWhosTurn(Party.FANTASYVALUE)
    with pytest.raises(AttributeError):
        ge.setWhosTurn("blubb")


def test_game_execution_check_player_assignment_correct(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.playerAssignmentCorrect() == True


def test_game_execution_check_player_assignment_incorrect_white(
    default_dynamics_tictactoe,
):
    pwhite = HumanPlayerTicTacToe(Party.BLACK)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.playerAssignmentCorrect() == False


def test_game_execution_check_player_assignment_incorrect_black(
    default_dynamics_tictactoe,
):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.WHITE)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.playerAssignmentCorrect() == False


def test_game_execution_opponent_party(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    with pytest.raises(AttributeError):
        ge.opponentParty(Party.NEUTRAL)


def test_game_execution_player_list(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    expected_player_list = [pwhite, pblack]
    assert ge.playerList() == expected_player_list


def test_change_turn_to_next(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.whosTurn() == Party.WHITE
    ge.changeTurnToNext()
    assert ge.whosTurn() == Party.BLACK
    ge.changeTurnToNext()
    assert ge.whosTurn() == Party.WHITE


def test_player_from_party(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    assert ge.playerFromParty(Party.WHITE) is ge.player_white
    assert ge.playerFromParty(Party.BLACK) is ge.player_black


def test_game_execution_current_player(default_dynamics_tictactoe):
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(default_dynamics_tictactoe, pwhite, pblack)
    ge.setWhosTurn(Party.WHITE)
    assert ge.currentPlayer() is ge.player_white
    ge.setWhosTurn(Party.BLACK)
    assert ge.currentPlayer() is ge.player_black


def test_game_execution_white_wins():
    line0 = "_XO\n"
    line1 = "O__\n"
    line2 = "XXX"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.WHITE_WINS
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome


def test_game_execution_eval_black_wins():
    line0 = "_OX\n"
    line1 = "X__\n"
    line2 = "OOO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.BLACK_WINS
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome


def test_game_execution_eval_draw():
    line0 = "XOX\n"
    line1 = "XXO\n"
    line2 = "OXO"
    state_string = line0 + line1 + line2
    board = BoardRectangular.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.DRAW
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome


def test_game_execution_execute_move(default_dynamics_tictactoe):
    dynamics = default_dynamics_tictactoe
    board = dynamics.board
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    point_for_testmove = CartPt(0, 0)
    ge.executeMove(ge.player_white, MoveTicTacToe(point_for_testmove, Party.WHITE))
    assert board.valueFromCartesian(point_for_testmove) == Party.WHITE


def test_request_move_from_player_fallback(default_dynamics_tictactoe):
    def fake_choose_move(self):
        return MoveTicTacToe(CartPt(0, 1), Party.WHITE)

    dynamics = default_dynamics_tictactoe
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    ge.setWhosTurn(ge.player2party_dct[ge.player_white])
    ge.player_white.chooseMove = MethodType(fake_choose_move, ge.player_white)
    board = dynamics.board
    board.setValueAtCartesian(CartPt(0, 1), Party.BLACK)
    with pytest.raises(ValueError):
        assert MoveTicTacToe(CartPt(0, 1), Party.WHITE) == ge.requestMoveFromPlayer(
            ge.player_white, 2
        )


def test_request_move_from_player_first_attempt_bad(default_dynamics_tictactoe):
    """Test Request move from player method. mock choose move result.
    first, chooseMove yields non-admissible move to test fallback.
    second, chooseMove yields legit move which should be the return
    value of request move from player
    """

    def fake_choose_move_gen():
        while True:
            yield MoveTicTacToe(CartPt(0, 1), Party.WHITE)
            yield MoveTicTacToe(CartPt(0, 0), Party.WHITE)

    def fake_choose_move(self):
        return next(self.testgen)

    dynamics = default_dynamics_tictactoe
    board = dynamics.board
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    ge.setWhosTurn(ge.player2party_dct[ge.player_white])

    ge.player_white.testgen = fake_choose_move_gen()
    ge.player_white.chooseMove = MethodType(fake_choose_move, ge.player_white)

    # occupy square CartPt(0,1)
    board.setValueAtCartesian(CartPt(0, 1), Party.BLACK)
    expected_move = MoveTicTacToe(CartPt(0, 0), Party.WHITE)
    obtained_move = ge.requestMoveFromPlayer(ge.player_white, 2)
    print(obtained_move)
    assert expected_move == obtained_move


def test_request_move_from_player(default_dynamics_tictactoe):
    def fake_choose_move(self):
        return MoveTicTacToe(CartPt(0, 1), Party.WHITE)

    dynamics = default_dynamics_tictactoe
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    ge.setWhosTurn(ge.player2party_dct[ge.player_white])
    ge.player_white.chooseMove = MethodType(fake_choose_move, ge.player_white)

    assert MoveTicTacToe(CartPt(0, 1), Party.WHITE) == ge.requestMoveFromPlayer(
        ge.player_white, 2
    )


def test_game_execution_display_result(default_dynamics_tictactoe, capsys):
    dynamics = default_dynamics_tictactoe
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    status = GameStatus.FAILURE
    ge.status = status
    ge.displayResult()
    captured = capsys.readouterr()
    captured = captured.out.strip()
    expected_substring = status.name
    assert expected_substring.lower() in captured.lower()

    status = GameStatus.WHITE_WINS
    ge.status = status
    ge.displayResult()
    captured = capsys.readouterr()
    captured = captured.out.strip()
    expected_substring = "WHITE"
    assert expected_substring.lower() in captured.lower() and "win" in captured.lower()

    status = GameStatus.BLACK_WINS
    ge.status = status
    ge.displayResult()
    captured = capsys.readouterr()
    captured = captured.out.strip()
    expected_substring = "BLACK"
    assert expected_substring.lower() in captured.lower() and "win" in captured.lower()

    status = GameStatus.DRAW
    ge.status = status
    ge.displayResult()
    captured = capsys.readouterr()
    captured = captured.out.strip()
    expected_substring = status.name
    assert expected_substring.lower() in captured.lower()


def test_game_execution_other_party(default_dynamics_tictactoe):
    dynamics = default_dynamics_tictactoe
    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    ge = GameExecution(dynamics, pwhite, pblack)
    assert ge.otherParty(Party.WHITE) == Party.BLACK
    assert ge.otherParty(Party.BLACK) == Party.WHITE
    with pytest.raises(ValueError):
        ge.otherParty(Party.NEUTRAL)
    with pytest.raises(ValueError):
        ge.otherParty(1895)


def test_game_execution_factory_default_noerror(monkeypatch):
    fake_kb_input_names = StringIO("\n\n")
    monkeypatch.setattr("sys.stdin", fake_kb_input_names)
    try:
        createDefaultTicTacToeGameExecutionHumanPlayers()
    except RuntimeError:
        pytest.fail("Factory Method leads to exception")


def test_game_execution_factory_fivewins_noerror(monkeypatch):
    fake_kb_input_names = StringIO("\n\n")
    monkeypatch.setattr("sys.stdin", fake_kb_input_names)
    try:
        createFiveWinsGameExecutionHumanPlayers()
    except RuntimeError:
        pytest.fail("Factory Method leads to exception")


def test_game_execution_factory_fourwinsgravity_noerror(monkeypatch):
    fake_kb_input_names = StringIO("\n\n")
    monkeypatch.setattr("sys.stdin", fake_kb_input_names)
    try:
        createFourWinsGravityGameExecutionHumanPlayers()
    except RuntimeError:
        pytest.fail("Factory Method leads to exception")
