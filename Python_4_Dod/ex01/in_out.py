def square(x: int | float) -> int | float:
    """return the square value"""
    return x * x


def pow(x: int | float) -> int | float:
    """return the exponential value of the argument by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    return an inner function that applies the given function to x,
    updates x and increments a count each time it is called.
    """
    if not isinstance(x, (int, float)):
        def error_func():
            print("The first argument must be an int or float.")
        return error_func
    if not callable(function):
        def error_func():
            print("The second argument must be a callable function.")
        return error_func

    count = 0

    def inner() -> float:
        """
        apply the given function to x, updates x with the result,
        increments the count, and returns the new result.
        """
        # use nonlocal to modify outer scope variables
        nonlocal count, x
        result = function(x)
        x = result
        count += 1
        return result

    return inner
