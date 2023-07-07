from game_execution import GameExecution, GameStatus
from Party import Party
import pytest
from human_player_tictactoe import HumanPlayerTicTacToe


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


# TODO: concept for key input or testplayer per generator?
# def test_smoke_test(default_dynamics_tictactoe):
#     dynamics = default_dynamics_tictactoe
#     ge = GameExecution(
#         dynamics, HumanPlayerTicTacToe(Party.WHITE), HumanPlayerTicTacToe(Party.BLACK)
#     )
#     ge.executeGame()
#     assert 1 == 0
