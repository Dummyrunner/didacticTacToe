from node import Node
import pytest


def test_node_init():
    n = Node(1)
    assert n.children == []
    assert n.data == 1


def test_node_append():
    n = Node(1)
    m = Node(5)
    n.addChild(m)
    assert len(n.children) == 1
    assert n.children == [m]
    with pytest.raises(AttributeError):
        n.addChild(333)
