def mean(args_sorted: list):
    """return the mean value"""
    return (sum(args_sorted) / len(args_sorted))


def median(args_sorted: list):
    """return the median value"""
    n = len(args_sorted)
    if (n % 2 != 0):
        return (args_sorted[n // 2])
    else:
        return (args_sorted[n // 2 - 1] + args_sorted[n // 2] / 2)


def quartile(args_sorted: list, q: int):
    """return the quartile value based on q"""
    n = len(args_sorted)
    if (q * n // 4 != 0):
        res = (args_sorted[q * n // 4])
    else:
        res = (args_sorted[q * n // 4 - 1] + args_sorted[q * n // 4] / 2)
    return float(res)


def variance(args_sorted: list):
    """return the variance value"""
    m = mean(args_sorted)
    var = (sum([float((arg - m) ** 2) for arg in args_sorted]))\
        / len(args_sorted)
    return var


def standard_deviation(args_sorted: list):
    """return the standard deviation value"""
    return float(variance(args_sorted) ** 0.5)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    input:  - args takes a a list of number
            - kwargs takes a statistic operation kyewords
    return: the results of each operations applied to the list
    """
    try:
        if not args:
            raise Exception
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise Exception
        args_sorted = sorted(args)
        results = {
            "mean": mean(args_sorted),
            "median": median(args_sorted),
            "quartile": [quartile(args_sorted, 1), quartile(args_sorted, 3)],
            "std": standard_deviation(args_sorted),
            "var": variance(args_sorted)
        }
        for key, value in kwargs.items():
            if value in results:
                print(f"{value} : {results[value]}")
            else:
                print("ERROR")
    except Exception:
        print("ERROR")
