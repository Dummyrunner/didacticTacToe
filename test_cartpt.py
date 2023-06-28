from board import CartPt


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
