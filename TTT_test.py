import TTT_Game
import sys

def test(func):
    def wrapper():
        try:
            func()
        except:
            print(f"{func.__name__ + ' failed':35} ❌")
        else:
            print(f"{func.__name__ + ' passed':35} ✅")
    wrapper._is_test = True
    return wrapper

@test
def testDraw():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(1, 0)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(2, 1)
    game.makeMove(1, 2)
    game.makeMove(0, 2)
    game.makeMove(2, 0)
    game.makeMove(2, 2)
    
    assert game.gameState == TTT_Game.GameState.Draw

@test
def testHorizontalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 0)
    game.makeMove(1, 1)
    game.makeMove(2, 0)

    assert game.gameState == TTT_Game.GameState.X_Won

@test
def testVerticalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(1, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

@test
def testPositiveDiagonalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(2, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 0)
    game.makeMove(0, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

@test
def testNegativeDiagonalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 2)
    game.makeMove(2, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

def runTests():

    current_module = sys.modules[__name__]


    for name in dir(current_module):
        obj = getattr(current_module, name)
        if callable(obj) and getattr(obj, "_is_test", False):
            obj()

if __name__ == '__main__':
    runTests()