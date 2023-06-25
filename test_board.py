import pytest
from enum import Enum
from board import Board, CartPt


@pytest.fixture
def default_board3x3():
    state_markers_dct = {"NEUTRAL": "_", "WHITE": "X", "BLACK": "O"}
    res = Board(state_markers_dct, 3, 3)
    return res


@pytest.fixture
def empty_states_default_board3x3():
    return 9 * ["_"]


def test_board_init(default_board3x3, empty_states_default_board3x3):
    assert default_board3x3.state == empty_states_default_board3x3


def test_board_set_value(default_board3x3):
    markers_dict = default_board3x3.state_markers_dict
    default_board3x3.setValueAtCartesian(CartPt(0, 0), markers_dict["BLACK"])
    default_board3x3.setValueAtCartesian(CartPt(1, 1), markers_dict["WHITE"])
    default_board3x3.setValueAtCartesian(CartPt(2, 2), markers_dict["NEUTRAL"])
    default_board3x3.setValueAtCartesian(CartPt(0, 1), markers_dict["WHITE"])
    expected_state = ["O", "_", "_", "X", "X", "_", "_", "_", "_"]
    assert default_board3x3.state == expected_state


def test_board_get_value(default_board3x3):
    markers_dict = default_board3x3.state_markers_dict
    given_state = ["O", "_", "_", "X", "X", "_", "_", "_", "_"]
    default_board3x3.setStateFromLinearList(given_state)
    assert default_board3x3.valueFromCartesian(CartPt(0, 0)) == markers_dict["BLACK"]
    assert default_board3x3.valueFromCartesian(CartPt(1, 1)) == markers_dict["WHITE"]
    assert default_board3x3.valueFromCartesian(CartPt(2, 2)) == markers_dict["NEUTRAL"]
    assert default_board3x3.valueFromCartesian(CartPt(0, 1)) == markers_dict["WHITE"]
