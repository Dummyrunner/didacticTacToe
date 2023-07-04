from Party import Party
from move_tictactoe import MoveTicTacToe
from cartpt import CartPt
from board import Board


class HumanPlayerTicTacToe:
    def __init__(self, party: Party, board: Board, name=""):
        if name == "":
            self.name = self.generate_name
        else:
            self.name = name
        self.party = party
        self.board = board

    def generate_name():
        ctr = 1
        while True:
            yield "Harald" + str(ctr)
            ctr += 1

    def chooseMove(self) -> MoveTicTacToe:
        print("Enter move for " + str(self.party) + " (Player " + self.name + "):")
        ip_string = self.getKeyBoardInput()
        return self.parseKeyboardInputToMove(ip_string)

    def getKeyBoardInput(self) -> str:
        ip = input(
            "move: X,Y, where X is the line from 0 to NumOfLines-1, Y column from 0 to NumOfColumns-1"
        )
        return ip

    def parseKeyboardInputToMove(self, ip: str):
        coords = [int(x) for x in ip.split(",")]
        x, y = coords
        return CartPt(x, y)
