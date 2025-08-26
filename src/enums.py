from enum import Enum
class Player(Enum):
    O = 0
    X = 1
    EMPTY = 2

    def switch(self):
        if self == Player.O:
            return Player.X
        elif self == Player.X:
            return Player.O
        else:  # EMPTY
            return Player.EMPTY
    
    def __str__(self):
        if self == Player.X:
            return "X"
        if self == Player.O:
            return "O"
        return " "
    
    def getWinState(self):
        if self == Player.O:
            return GameState.O_Won
        if self == Player.X:
            return GameState.X_Won
        return

class GameState(Enum):
    OnGoing = 0
    Draw = 1
    X_Won = 2
    O_Won = 3