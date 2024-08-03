class calculator:
    """Calculator that does arithmetics operations on vectors"""

    def __init__(self, vector):
        """Constructor for the vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """sum operation"""
        self.vector = [v + object for v in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """multiplication operation"""
        self.vector = [v * object for v in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """substraction operation"""
        self.vector = [v - object for v in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """division operation"""
        try:
            if object == 0:
                raise ZeroDivisionError("cannot divide by 0")
            self.vector = [v / object for v in self.vector]
            print(self.vector)
            return self.vector
        except ZeroDivisionError as z:
            print(ZeroDivisionError.__name__ + ":", z)
