from node import Node
from tree import Tree
import pytest


def test_tree_init():
    rootnode = Node(1)
    t = Tree(rootnode)
    assert t.root.data == 1
    with pytest.raises(AttributeError):
        t_fail = Tree("STRING_IS_UNWANTED_HERE")
