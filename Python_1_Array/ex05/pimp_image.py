import array  # for flake8 norm
import numpy as np
from PIL import Image


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    inverted = 255 - array
    Image.fromarray(inverted).show()


def ft_red(array) -> array:
    """Set other color channels to 0 except for red."""
    red = array.copy()
    # sets the Green channel to 0
    red[:, :, 1] = 0
    # sets the Blue channel to 0
    red[:, :, 2] = 0
    Image.fromarray(red).show()


def ft_green(array) -> array:
    """Set other color channels to 0 except for green."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    Image.fromarray(green).show()


def ft_blue(array) -> array:
    """Set other color channels to 0 except for blue."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Image.fromarray(blue).show()


def ft_grey(array) -> array:
    """Converts the image to grayscale."""
    grey = (
        array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
    )
    # np.repeat(a, repeats, axis=None)
    # repeats elements of an array and can be used
    # to repeat elements along a specified axis
    grayscaled = np.repeat(grey[:, :, np.newaxis], 3, axis=2)
    # astype is a method used to cast the elements of an array
    # to np.uint8 type representing an 8-bit unsigned integer
    Image.fromarray(grayscaled.astype(np.uint8)).show()
