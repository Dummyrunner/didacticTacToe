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
    assert len(t.bfsTraversal(t.root)) == 1
    assert [node.data for node in t.bfsTraversal(t.root)] == [1]


def test_tree_bfs_traversal(four_node_tree: Tree):
    t = four_node_tree
    assert [node.data for node in t.bfsTraversal(t.root)] == [1, 2, 3, 4]


def test_tree_dfs_travesal_minimal():
    rootnode = Node(1)
    t = Tree(rootnode)
    assert len(t.dfsTraversal(t.root)) == 1
    assert [node.data for node in t.dfsTraversal(t.root)] == [1]


def test_tree_dfs_traversal(four_node_tree: Tree):
    t = four_node_tree
    assert [node.data for node in t.dfsTraversal(t.root)] == [1, 2, 4, 3]


def test_tree_to_str_line():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.addChild(n2)
    n2.addChild(n3)
    t = Tree(n1)
    line0 = "1\n"
    line1 = "#2\n"
    line2 = "##3.\n"
    expected_string = line0 + line1 + line2
    assert expected_string == str(t)


def test_tree_to_str_line_two_nodes():
    n1 = Node(1)
    n2 = Node(2)
    n1.addChild(n2)
    t = Tree(n1)
    line0 = "1\n"
    line1 = "#2.\n"
    expected_string = line0 + line1
    assert expected_string == str(t)


def test_tree_to_str(four_node_tree):
    t = four_node_tree
    line0 = "1\n"
    line1 = "#2\n"
    line2 = "##4.\n"
    line3 = "#3.\n"
    expected_string = line0 + line1 + line2 + line3
    assert expected_string == str(t)


def test_tree_to_str_one_node():
    n = Node(1)
    t = Tree(n)
    expected_string = "1.\n"
    assert expected_string == str(t)
