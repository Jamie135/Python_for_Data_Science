def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI values based on given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """
    try:
        if len(height) != len(weight):
            raise Exception("lists sizes are different")
        bmi = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                or not isinstance(w, (int, float)) \
                    or h <= 0 or w <= 0:
                raise Exception("must be a list of positive int or float")
            bmi.append(w / (h ** 2))
        return bmi
    except Exception as e:
        print(f"Error: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether BMI values are above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.
    """
    try:
        if not isinstance(limit, int) and not isinstance(limit, float):
            raise Exception("limit must be an int or float.")
        isabove = []
        for item in bmi:
            if not isinstance(item, (int, float)):
                raise Exception("bmi values must be an int or float")
            isabove.append(item > limit)
        return isabove
    except Exception as e:
        print(f"Error: {e}")
