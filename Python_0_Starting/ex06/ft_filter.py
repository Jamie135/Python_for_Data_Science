def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object
    Return an iterator yielding those items
    of iterable for which function(item)"""
    if function is None:
        function = bool
    return (item for item in iterable if function(item))


# print(ft_filter.__doc__)
