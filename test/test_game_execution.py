from game_execution import GameExecution, GameStatus
from Party import Party
import pytest
from player_tictactoe import HumanPlayerTicTacToe
from board import Board
from game_dynamics_tictactoe import GameDynamicsTicTacToe


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


# TODO remove, test new eval fucntion instead
def test_game_execution_white_wins():
    line0 = "_XO\n"
    line1 = "O__\n"
    line2 = "XXX"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.WHITE_WINS
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome


# TODO test _inputTopologyValid
def test_input_topology_valid():
    pass


def test_game_execution_black_wins():
    line0 = "_OX\n"
    line1 = "X__\n"
    line2 = "OOO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.BLACK_WINS
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome


def test_game_execution_draw():
    line0 = "XOX\n"
    line1 = "XXO\n"
    line2 = "OXO"
    state_string = line0 + line1 + line2
    board = Board.fromString(state_string)

    pwhite = HumanPlayerTicTacToe(Party.WHITE)
    pblack = HumanPlayerTicTacToe(Party.BLACK)
    rowsize_to_win = 3
    dyn = GameDynamicsTicTacToe(board, rowsize_to_win)
    ge = GameExecution(dyn, pwhite, pblack)
    expected_outcome = GameStatus.DRAW
    actual_outcome = ge.evaluateGameState()
    assert expected_outcome == actual_outcome
