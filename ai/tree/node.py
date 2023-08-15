class Node:
    def __init__(self, data):
        self.__data = data
        self.__children = []

    @property
    def data(self):
        return self.__data

    @property
    def children(self):
        return self.__children

    def addChild(self, child):
        if type(child) == Node:
            self.children.append(child)
        else:
            raise AttributeError("Wrong type. Children of nodes have to be nodes")
