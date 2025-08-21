import TTT_Game
import TTT_Enums
import sys

def test(func):
    def wrapper():
        try:
            func()
        except AssertionError:
            print(f"{func.__name__ + ' failed':35} ❌")
        except Exception as _:
            raise
        else:
            print(f"{func.__name__ + ' passed':35} ✅")
    wrapper._is_test = True
    return wrapper

def gameTest(func):
    wrapper = test(func)
    wrapper._is_gameTest = True
    return wrapper


@gameTest
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

@gameTest
def testHorizontalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 0)
    game.makeMove(1, 1)
    game.makeMove(2, 0)

    assert game.gameState == TTT_Game.GameState.X_Won

@gameTest
def testVerticalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(1, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

@gameTest
def testPositiveDiagonalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(2, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 0)
    game.makeMove(0, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

@gameTest
def testNegativeDiagonalWin():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 2)
    game.makeMove(2, 2)

    assert game.gameState == TTT_Game.GameState.X_Won

@gameTest
def testClearFunction():
    game = TTT_Game.Game(TTT_Game.Player.X)
    game.makeMove(0, 0)
    game.makeMove(0, 1)
    game.makeMove(1, 1)
    game.makeMove(0, 2)
    game.makeMove(2, 2)
    game.clear()
    for i in game.grid:
        for j in i:
            assert j == TTT_Enums.Player.EMPTY
    assert game.gameState == TTT_Enums.GameState.OnGoing

@gameTest
def testInvalidMoves():
    game = TTT_Game.Game(TTT_Game.Player.X)
    try:     
        game.makeMove(3, 0)
    except Exception as e:
        assert isinstance(e, ValueError)
    else:
        assert False
    try:
        game.makeMove(0, 0)
        game.makeMove(0, 0)
    except Exception as e:
        assert isinstance(e, ValueError)
    else:
        assert False  
    game.clear()
    try:
        game.makeMove(0, 0)
        game.makeMove(0, 1)
        game.makeMove(1, 1)
        game.makeMove(0, 2)
        game.makeMove(2, 2)
        game.makeMove(0, 0)
    except Exception as e:
        assert isinstance(e, RuntimeError)
    else:
        assert False

def runTests(testAttr = '_is_test'):

    current_module = sys.modules[__name__]


    for name in dir(current_module):
        obj = getattr(current_module, name)
        if callable(obj) and getattr(obj, testAttr, False):
            obj()

if __name__ == '__main__':
    runTests()