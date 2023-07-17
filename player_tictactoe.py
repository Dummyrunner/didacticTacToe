from Party import Party
from move_tictactoe import MoveTicTacToe
from cartpt import CartPt
from board import Board


class BasePlayerTicTacToe:
    def __init__(self, party: Party, name=""):
        self.name = name
        self.party = party
        self.board = None

    def _inputTopologyValid(self, ip_string: str, split_char=",") -> bool:
        """True, if input string ip_string contanins two integer values
        separated by one split character, by default a comma"""
        how_many_commas = ip_string.count(split_char)
        if how_many_commas != 1:
            return False
        x, y = ip_string.split(split_char)
        return x.isdigit() and y.isdigit()

    def updateBoard(self, new_board):
        self.board = new_board


class HumanPlayerTicTacToe(BasePlayerTicTacToe):
    def chooseMove(self, max_tries=2) -> MoveTicTacToe:
        print("Your turn, " + str(self.party.name + "! ") + "(name: " + self.name + ")")
        for num_of_tries in range(0, max_tries):
            ip_string = self.getKeyBoardInput()
            if self._inputTopologyValid(ip_string):
                return self.parseKeyboardInputToMove(ip_string)
            num_of_tries += 1
            print(
                "Input has not the right topology to represent a move. try again! Bad topology input ("
                + str(num_of_tries)
                + "/"
                + str(max_tries)
                + ")"
            )
        raise ValueError(
            "Repeatedly bad topology: Max num " + str(max_tries) + " exceeded"
        )

    def getKeyBoardInput(self) -> str:
        max_row_idx = self.board.numOfRows() - 1
        max_col_idx = self.board.numOfCols() - 1
        ip = input(
            'move: Enter "X,Y" where X is the row index from 0 to '
            + str(max_row_idx)
            + ", Y column index from 0 to "
            + str(max_col_idx)
            + ":\n"
        )
        return ip

    def parseKeyboardInputToMove(self, ip: str):
        coords = [int(x) for x in ip.split(",")]
        x, y = coords
        pt = CartPt(x, y)
        return MoveTicTacToe(pt, self.party)
