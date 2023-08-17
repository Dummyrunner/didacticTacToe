from node import Node


class Tree:
    def __init__(self, root: Node):
        if type(root) != Node:
            raise AttributeError("Error creating tree: root has to be of Node type")
        self.root = root

    def BFSTraversal(self, root):
        pass


class NodeQueue:
    def __init__(self, initial_queue=[]):
        self.queue = initial_queue

    def pop(self):
        raise NotImplementedError

    def push(self):
        raise NotImplementedError


class NodeQueueFIFO(NodeQueue):
    def __init__(self, initial_queue):
        self.super().__init__(initial_queue)

    def pop(self):
        pass

    def push(self):
        pass
