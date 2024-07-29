import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes a 2D list, prints its shape, and returns a truncated version
    based on the provided start and end arguments."""
    try:
        # error handling
        if not isinstance(family, list) or not family:
            raise Exception("family must be a non-empty list")
        size = len(family[0])
        for lst in family:
            if not isinstance(lst, list) or len(lst) != size:
                raise Exception("must be lists of the same length")
            if not all(isinstance(item, (int, float)) for item in lst):
                raise Exception("list's element must an int or float")
        # convert the list into ndarray
        # to be able to apply numpy
        npfamily = np.array(family)
        print(f"My shape is : {npfamily.shape}")
        truncated = npfamily[start:end, :]
        print(f"My new shape is : {truncated.shape}")
        return truncated

    except Exception as e:
        print(f"Error: {e}")
