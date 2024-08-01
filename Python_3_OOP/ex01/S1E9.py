from abc import ABC, abstractmethod


class Character(ABC):
    """Class representing a character from any universe"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for the character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to kill a character"""
        pass


class Stark(Character):
    """Class representing Stark inherited from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to kill Stark"""
        self.is_alive = False
