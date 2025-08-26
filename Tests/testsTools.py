import sys

def test(func, attr = "_is_test"):
    def wrapper():
        try:
            func()
        except AssertionError:
            print(f"{func.__name__ + ' failed':35} ❌")
        except Exception as _:
            raise
        else:
            print(f"{func.__name__ + ' passed':35} ✅")
    setattr(wrapper, attr, True)
    return wrapper

def runTests(testAttr = '_is_test'):

    current_module = sys.modules["__main__"]


    for name in dir(current_module):
        obj = getattr(current_module, name)
        if callable(obj) and getattr(obj, testAttr, False):
            obj()