from node import Node
from tree import Tree
import pytest


@pytest.fixture
def four_node_tree():
    rootnode = Node(1)
    a1 = Node(2)
    a2 = Node(3)
    b1 = Node(4)
    rootnode.addChild(a1)
    rootnode.addChild(a2)
    a1.addChild(b1)
    return Tree(rootnode)


def test_tree_init():
    rootnode = Node(1)
    t = Tree(rootnode)
    assert t.root.data == 1
    with pytest.raises(AttributeError):
        t_fail = Tree("STRING_IS_UNWANTED_HERE")


def test_tree_bfs_travesal_minimal():
    rootnode = Node(1)
    t = Tree(rootnode)
    assert len(t.BFSTraversal(t.root)) == 1
    assert [node.data for node in t.BFSTraversal(t.root)] == [1]


def test_tree_bfs_traversal(four_node_tree):
    t = four_node_tree
    assert [node.data for node in t.BFSTraversal(t.root)] == [1, 2, 3, 4]
