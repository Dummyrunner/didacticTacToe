from node import Node
from queue import Queue, LifoQueue


class Tree:
    def __init__(self, root: Node):
        if type(root) != Node:
            raise AttributeError("Error creating tree: root has to be of Node type")
        self.root = root

    def bfsTraversal(self, start_node: Node):
        result_list = []
        queue = Queue()
        queue.put(start_node)
        while not queue.empty():
            next_node = queue.get()
            result_list.append(next_node)
            [queue.put(childnode) for childnode in next_node.children]
        return result_list

    def dfsTraversal(self, start_node: Node):
        result_list = []
        queue = LifoQueue()
        queue.put(start_node)
        while not queue.empty():
            next_node = queue.get()
            result_list.append(next_node)
            [queue.put(childnode) for childnode in reversed(next_node.children)]
        return result_list
