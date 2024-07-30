import os  # for path check
import array  # for flake8 norm
import numpy as np
from PIL import Image


def ft_load(path: str) -> array:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise Exception("only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise Exception("no such file or directory")
        img = Image.open(path)
        # use array() to convert the img object into array
        img_array = np.array(img)
        print(f"The shape of image is: "
              f"({img_array.shape[0]}, {img_array.shape[1]})")
        return (img_array)
    except Exception as e:
        print(f"Error: {e}")
        return ""
