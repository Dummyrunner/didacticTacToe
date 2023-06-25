class CartPt:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class Board:
    def __init__(self, state_markers_dict, size_x=3, size_y=3):
        self.SIZE_X = size_x
        self.SIZE_Y = size_y
        state_marker_list = ["_", "x", "o"]
        self.state_markers_dict = state_markers_dict
        num_of_squares = size_x * size_y
        self.__state = [state_markers_dict["NEUTRAL"] for i in range(0, num_of_squares)]

    def setValueAtCartesian(self, cart_pt, new_val):
        x = cart_pt.x
        y = cart_pt.y
        self.__state[self.SIZE_X * y + x] = new_val

    def valueFromCartesian(self, CartPt):
        x = CartPt.x
        y = CartPt.y
        return self.__state[self.SIZE_X * y + x]

    def setStateFromLinearList(self, input_list):
        self.__state = input_list

    @property
    def state(self):
        return self.__state

    def __str__(self):
        res = ""
        for char in self.__state:
            res += char
        return res
