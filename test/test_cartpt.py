from board import CartPt
from pytest import raises


def test_access_coordinates():
    test_x = 3
    test_y = 5
    p = CartPt(test_x, test_y)
    assert p.x == test_x
    assert p.y == test_y


def test_print_cartpt():
    test_x = 3
    test_y = 5
    p = CartPt(test_x, test_y)
    expected_string = "(3,5)"
    assert str(p) == expected_string


def test_cartpt_euqality_operator():
    pt1 = CartPt(0, 0)
    pt2 = CartPt(0, 0)
    pt3 = CartPt(0, 1)
    assert pt1 == pt2
    assert pt1 != pt3
    with raises(AssertionError):
        assert pt1 == 333
