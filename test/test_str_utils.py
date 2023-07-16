from str_utils import *


def test_str_in_box_tight():
    expected_str = "####\n" + "#HI#\n" + "####"
    assert strInBox("HI", 4, "#") == expected_str
    expected_str = "~~~~\n" + "~HI~\n" + "~~~~"
    assert strInBox("HI", 4, "~") == expected_str


def test_str_in_box_loose():
    expected_str = "########\n" + "#  HI  #\n" + "########"
    assert strInBox("HI", 8, "#") == expected_str


def test_str_in_box_boxlen_too_small():
    expected_str = "####\n" + "#HI#\n" + "####"
    assert strInBox("HI", 3, "#") == expected_str
