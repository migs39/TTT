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

class Game:
    def __init__(self, firstPlayer):

        if not isinstance(firstPlayer, Player):
            raise TypeError("firstPlayer precisa ser um Cell")
        if firstPlayer == Player.EMPTY:
            raise ValueError("firstPlayer não pode ser EMPTY")
        
        self.grid = [[Player.EMPTY, Player.EMPTY, Player.EMPTY], 
                     [Player.EMPTY, Player.EMPTY, Player.EMPTY],
                     [Player.EMPTY, Player.EMPTY, Player.EMPTY]]
        self.currentPlayer = firstPlayer
        self.gameState = GameState.OnGoing

    def updateGameState(self):
        for player in [Player.X, Player.O]:

            #checks horizontal lines
            for i in self.grid:
                winning = True
                for j in i:
                    winning = winning and j == player
                if winning:
                    self.gameState = player.getWinState()
                    return
            
            #checks vertical lines
            for i in range(3):
                winning = True
                for j in self.grid:
                    winning = winning and j[i] == player
                if winning:
                    self.gameState = player.getWinState()
                    return
            
            #checks positive diagonal
            winning = True
            for i in range(3):
                winning = winning and self.grid[i][2-i] == player
            if winning:
                self.gameState = player.getWinState()
                return
            #checks negative diagonal
            winning = True
            for i in range(3):
                winning = winning and self.grid[i][i] == player
            if winning:
                self.gameState = player.getWinState()
                return

            for i in self.grid:
                for j in i:
                    if j == Player.EMPTY:
                        self.gameState = GameState.OnGoing
                        return
            self.gameState = GameState.Draw
            return

    def makeMove(self, x, y):

        if self.gameState != GameState.OnGoing:
            raise Exception("Game is over")
        
        if x not in range(3) or y not in range(3) or self.grid[y][x] != Player.EMPTY:
            raise Exception("Invalid move")
        
        self.grid[y][x] = self.currentPlayer
        self.currentPlayer = self.currentPlayer.switch()
        self.updateGameState()
    
    def __str__(self):
        return(
        f'\n{self.grid[0][0]}|{self.grid[0][1]}|{self.grid[0][2]}'
        "\n------"
        f'\n{self.grid[1][0]}|{self.grid[1][1]}|{self.grid[1][2]}'
        "\n------"
        f'\n{self.grid[2][0]}|{self.grid[2][1]}|{self.grid[2][2]}\n')

if __name__ == "__main__":
    game = Game(Player.X)
    while game.gameState == GameState.OnGoing:
        print(game)
        print(f"{game.currentPlayer}'s turn")
        print(f"what collumn do you want to place an {game.currentPlayer}?")
        moveCollumn = int(input()) - 1
        print(f"what line do you want to place an {game.currentPlayer}?")
        moveLine = int(input()) - 1
        try:
            game.makeMove(moveCollumn, moveLine)
        except Exception as e:
            if str(e) == "Invalid move":
                print(e)
            else:
                raise
    print("game ended")
    if game.gameState == GameState.Draw:
        print("it was a Draw")
    if game.gameState == GameState.X_Won:
        print("X won")
    if game.gameState == GameState.O_Won:
        print("O won")