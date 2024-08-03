from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        string information about Baratheon attribute
        """
        return "{}, {}, {}".format(self.family_name, self.eyes, self.hairs)

    def __repr__(self):
        """
        representation for Baratheon Class instance
        """
        return "Vector: ('{}', '{}', '{}')".format(self.family_name,
                                                   self.eyes,
                                                   self.hairs)

    def die(self):
        """Method to kill Baratheon"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        string information about Lannister attribute
        """
        return "{}, {}, {}".format(self.family_name,
                                   self.eyes,
                                   self.hairs)

    def __repr__(self):
        """
        representation for Lannister Class instance
        """
        return "Vector: ('{}', '{}', '{}')".format(self.family_name,
                                                   self.eyes,
                                                   self.hairs)

    def die(self):
        """Method to kill Lannister"""
        self.is_alive = False

    @classmethod
    def create_lannister(self, first_name, is_alive):
        """
        Create a Lannister character instance.
        """
        return Lannister(first_name, is_alive)
