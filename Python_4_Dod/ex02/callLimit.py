def callLimit(limit: int):
    """
    Takes an integer 'limit' and returns a decorator that restricts
    the number of times a decorated function can be called.
    If the function is called more times than the
    limit, a 'AssertionError' is raised.
    """

    count = 0

    def callLimiter(function):
        """
        Decorator:
        This inner function is used to wrap around the target function.
        It tracks the number of times the target function is called.
        If the function has been called less than or equal
        to the specified 'limit', it allows the function's execution.
        If the limit is exceeded, it raises a 'ValueError'.
        """

        def limit_function(*args: any, **kwds: any):
            """
            Wrapper:
            Used as a wrapper around the decorated function.
            It increments the 'count' variable each time the wrapped
            function is called. If the 'count' is within the limit,
            the wrapped function is executed. Otherwise, an 'AssertionError'
            is raised indicating that the function has been called too
            many times.
            """

            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
