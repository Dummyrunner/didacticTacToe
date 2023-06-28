from board import CartPt


def test_access_coordinates():
    test_x = 3
    test_y = 5
    p = CartPt(test_x, test_y)
    assert p.x == test_x
    assert p.y == test_y
