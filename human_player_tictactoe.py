from Party import Party
from move_tictactoe import MoveTicTacToe
from cartpt import CartPt
from board import Board


class HumanPlayerTicTacToe:
    def __init__(self, party: Party, name=""):
        if name == "":
            self.name = next(self.generate_name())
        else:
            self.name = name
        self.party = party
        self.board = None

    def generate_name(self):
        ctr = 1
        while True:
            yield "Harald" + str(ctr)
            ctr += 1

    def chooseMove(self) -> MoveTicTacToe:
        print("party " + str(self.party))
        print("name: " + self.name)

        print("Enter move for " + str(self.party) + " (Player " + self.name + "):")
        ip_string = self.getKeyBoardInput()
        return self.parseKeyboardInputToMove(ip_string)

    def _inputTopologyValid(self, ip_string: str, split_char=",") -> bool:
        """True, if input string ip_string contanins two integer values
        separated by one split character, by default a comma"""
        how_many_commas = ip_string.count(split_char)
        if how_many_commas != 1:
            return False
        x, y = ip_string.split(split_char)
        return x.isdigit() and y.isdigit()

    def getKeyBoardInput(self) -> str:
        ip = input(
            "move: X,Y, where X is the line from 0 to NumOfLines-1, Y column from 0 to NumOfColumns-1:\n"
        )
        return ip

    def parseKeyboardInputToMove(self, ip: str):
        coords = [int(x) for x in ip.split(",")]
        x, y = coords
        pt = CartPt(x, y)
        return MoveTicTacToe(pt, self.party)

    def updateBoard(self, new_board):
        self.board = new_board
