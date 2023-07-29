from enum import Enum


class GameStatus(Enum):
    PREPARE = 0
    RUNNING = 1
    WHITE_WINS = 2
    BLACK_WINS = 3
    DRAW = 4
    FAILURE = 5
