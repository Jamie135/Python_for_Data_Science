from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for then King
        inherited from Baratheon and Lannister"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes) -> str:
        """set eye's color"""
        self.eyes = eyes

    def set_hairs(self, hairs) -> str:
        """set hair's color"""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """return eye's color"""
        return self.eyes

    def get_hairs(self) -> str:
        """return hair's color"""
        return self.hairs
