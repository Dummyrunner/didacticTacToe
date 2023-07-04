from game_execution import GameExecution, GameStatus
from Party import Party
import pytest


def test_game_execution_init(default_dynamics_tictactoe):
    ge = GameExecution(default_dynamics_tictactoe)
    assert ge.whosTurn() == Party.WHITE
    ge.setWhosTurn(Party.BLACK)
    assert ge.whosTurn() == Party.BLACK
    assert ge.winner == Party.NEUTRAL
    assert ge.status == GameStatus.PREPARE


def test_game_execution_init_fail(default_dynamics_tictactoe):
    ge = GameExecution(default_dynamics_tictactoe)
    with pytest.raises(AttributeError):
        ge.setWhosTurn(Party.NEUTRAL)
    with pytest.raises(AttributeError):
        ge.setWhosTurn(Party.FANTASYVALUE)
    with pytest.raises(AttributeError):
        ge.setWhosTurn("blubb")
