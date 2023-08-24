from enum import Enum


class GameStatus(Enum):
    PREPARE = 2
    RUNNING = 3
    WHITE_WINS = +1
    BLACK_WINS = -1
    DRAW = 0
    FAILURE = 4
