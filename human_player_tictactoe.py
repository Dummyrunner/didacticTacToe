from Party import Party


class HumanPlayerTicTacToe:
    def __init__(self, party: Party, name=""):
        if name == "":
            self.name = self.generate_name
        else:
            self.name = name
        self.party = party

    def generate_name():
        ctr = 1
        while True:
            yield "Harald" + str(ctr)
            ctr += 1

    def chooseMove(self):
        # TODO
        pass
