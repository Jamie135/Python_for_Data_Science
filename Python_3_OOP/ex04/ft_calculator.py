class calculator:
    """Calculator that does arithmetics operations between vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """sum operation"""
        v = [round(float(v1 * v2), 1) for v1, v2 in zip(V1, V2)]
        n = sum(x for x in v)
        print(f"Dot product is: {n}")
        return n

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """multiplication operation"""
        v = [round(float(v1 + v2), 1) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is: {v}")
        return v

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substraction operation"""
        v = [round(float(v1 - v2), 1) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {v}")
        return v
