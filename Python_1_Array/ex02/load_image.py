import os  # for path check
import array  # for flake8 norm
import numpy as np
from PIL import Image


def ft_load(path: str) -> array:
    try:
        if not os.path.exists(path):
            raise Exception("no such file or directory")
        # context manager to help close file in case of error
        with Image.open(path) as img:
            # use array() to convert the img object into array of float32
            img_array = np.array(img)
            print(f"The shape of image is: "
                  f"({img_array.shape[0]}, {img_array.shape[1]},"
                  f" {len(img_array[0][0])})")
            return (img_array)
    # OSError handles the error from context manager
    except OSError as oserr:
        print(f"OSError: {oserr}")
    except Exception as e:
        print(f"Error: {e}")
