# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if not isinstance(x, int):
        raise ValueError("Unsupported type of x")
    if not isinstance(y, int):
        raise ValueError("Unsupported type of y")
    if 0 > x or x > 100:
        raise ValueError("Argument x isn't in the correct range")
    if 0 > y or y > 100:
        raise ValueError("Argument x isn't in the correct range")

    return x + y
