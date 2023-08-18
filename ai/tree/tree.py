from node import Node
from queue import Queue, LifoQueue


class Tree:
    def __init__(self, root: Node):
        if type(root) != Node:
            raise AttributeError("Error creating tree: root has to be of Node type")
        self.root = root

    def BFSTraversal(self, root):
        pass
