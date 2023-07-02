class CartPt:
    """Cartesian point. holds two attributes x and y. x represents the row number,
    y the column number"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        string = "(" + str(self.x) + "," + str(self.y) + ")"
        return string

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        if not isinstance(other, CartPt):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
