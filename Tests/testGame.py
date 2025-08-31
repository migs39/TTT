import src.game as game
import src.enums as enums
from .testsTools import test
from .testsTools import runTests

@test
def testEquals():
    game1 = game.Game(game.Player.X)
    game1.makeMove(0, 0)
    game2 = game.Game(game.Player.X)
    assert not game2 == game1
    game2.makeMove(0, 0)
    assert game1 == game2
    game2.currentPlayer = game2.currentPlayer.switch()
    assert game1 != game2

@test
def testIsEquivalent():
    game1 = game.Game(game.Player.X)
    game2 = game.Game(game.Player.X)

    game1.grid = [[enums.Player.O, enums.Player.EMPTY, enums.Player.X],
                 [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                 [enums.Player.O, enums.Player.EMPTY, enums.Player.EMPTY]]
    
    game2.grid = [[enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.EMPTY],
                  [enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.EMPTY],
                  [enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.EMPTY]]
    
    assert not game1.isEquivalent(game2)
    assert not game2.isEquivalent(game1)

    game2.grid = [[enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.X],
                  [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                  [enums.Player.O, enums.Player.EMPTY, enums.Player.O]]
    
    assert game1.isEquivalent(game2)
    assert game2.isEquivalent(game1)

@test
def testRotate():
    game1 = game.Game(game.Player.X)
    game1.grid = [[enums.Player.O, enums.Player.EMPTY, enums.Player.X],
                 [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                 [enums.Player.O, enums.Player.EMPTY, enums.Player.EMPTY]]
    game2 = game1.copy()
    game1.rotate()
    game3 = game.Game(game.Player.X)
    game3.grid = [[enums.Player.O, enums.Player.EMPTY, enums.Player.O],
                  [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                  [enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.X]]
    assert game1 == game3
    game1.rotate()
    game1.rotate()
    game1.rotate()
    assert game1 == game2

@test
def testMirror():
    game1 = game.Game(game.Player.X)
    game1.grid = [[enums.Player.O, enums.Player.EMPTY, enums.Player.X],
                 [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                 [enums.Player.O, enums.Player.EMPTY, enums.Player.EMPTY]]
    game2 = game1.copy()
    game1.mirrorGrid()
    game3 = game.Game(game.Player.X)
    game3.grid = [[enums.Player.X, enums.Player.EMPTY, enums.Player.O],
                  [enums.Player.EMPTY, enums.Player.X, enums.Player.EMPTY],
                  [enums.Player.EMPTY, enums.Player.EMPTY, enums.Player.O]]
    assert game1 == game3
    game1.mirrorGrid()
    assert game1 == game2

@test
def testDraw():
    game1 = game.Game(game.Player.X)
    game1.makeMove(1, 0)
    game1.makeMove(0, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 1)
    game1.makeMove(2, 1)
    game1.makeMove(1, 2)
    game1.makeMove(0, 2)
    game1.makeMove(2, 0)
    game1.makeMove(2, 2)
    
    assert game1.gameState == game.GameState.Draw

@test
def testHorizontalWin():
    game1 = game.Game(game.Player.X)
    game1.makeMove(0, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 0)
    game1.makeMove(1, 1)
    game1.makeMove(2, 0)

    assert game1.gameState == game.GameState.X_Won

@test
def testVerticalWin():
    game1 = game.Game(game.Player.X)
    game1.makeMove(0, 0)
    game1.makeMove(1, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 1)
    game1.makeMove(0, 2)

    assert game1.gameState == game.GameState.X_Won

@test
def testPositiveDiagonalWin():
    game1 = game.Game(game.Player.X)
    game1.makeMove(2, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 1)
    game1.makeMove(0, 0)
    game1.makeMove(0, 2)

    assert game1.gameState == game.GameState.X_Won

@test
def testNegativeDiagonalWin():
    game1 = game.Game(game.Player.X)
    game1.makeMove(0, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 1)
    game1.makeMove(0, 2)
    game1.makeMove(2, 2)

    assert game1.gameState == game.GameState.X_Won

@test
def testClearFunction():
    game1 = game.Game(game.Player.X)
    game1.makeMove(0, 0)
    game1.makeMove(0, 1)
    game1.makeMove(1, 1)
    game1.makeMove(0, 2)
    game1.makeMove(2, 2)
    game1.clear()
    for i in game1.grid:
        for j in i:
            assert j == enums.Player.EMPTY
    assert game1.gameState == enums.GameState.OnGoing

@test
def testInvalidMoves():
    game1 = game.Game(game.Player.X)
    try:     
        game1.makeMove(3, 0)
    except Exception as e:
        assert isinstance(e, ValueError)
    else:
        assert False
    try:
        game1.makeMove(0, 0)
        game1.makeMove(0, 0)
    except Exception as e:
        assert isinstance(e, ValueError)
    else:
        assert False  
    game1.clear()
    try:
        game1.makeMove(0, 0)
        game1.makeMove(0, 1)
        game1.makeMove(1, 1)
        game1.makeMove(0, 2)
        game1.makeMove(2, 2)
        game1.makeMove(0, 0)
    except Exception as e:
        assert isinstance(e, RuntimeError)
    else:
        assert False
    return

@test
def testRepr():
    game1 = game.Game(enums.Player.X)
    assert repr(game1) == "EEEEEEEEE"
    game1.makeMove(0, 0)
    assert repr(game1) == "XEEEEEEEE"
    game1.makeMove(1, 1)
    assert repr(game1) == "XEEEOEEEE"
    game1.makeMove(2, 2)
    assert repr(game1) == "XEEEOEEEX"
    game1.makeMove(0, 2)
    assert repr(game1) == "XEEEOEOEX"
    game1.makeMove(2, 0)
    assert repr(game1) == "XEXEOEOEX"
    game1.makeMove(1, 0)
    assert repr(game1) == "XOXEOEOEX"
    game1.makeMove(2, 1)
    assert repr(game1) == "XOXEOXOEX"

if __name__ == '__main__':
    runTests()