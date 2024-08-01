import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def display_first(arr):
    """
    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner.
    """
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            print("[[[", row[0], "]", sep="")
        if count > 0 and count < 3 or count > length - 4:
            if count == length - 1:
                print("  [", row[0], "]]]", sep="")
            elif count < length - 1:
                print("  [", row[0], "]", sep="")
        if count == 2:
            print("  ...")
        count += 1


def transpose_img(image):
    """
    Transpose the input image (PIL.Image.Image)
    by swapping its width and height dimensions.
    """
    rows, cols = image.size
    transposed = Image.new("RGB", (cols, rows))

    for j in range(cols):
        for i in range(rows):
            pixel = image.getpixel(((i, j)))
            transposed.putpixel((j, i), pixel)
    return transposed


def main():
    """
    This function serves as the main entry point of the script.
    It loads animal.jpeg, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and rotated image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = "../resources/animal.jpeg"
        image = Image.open(path)
        if image is None:
            raise AssertionError("failed to load image.")

        cropped = image.crop((400, 200, 800, 600))
        # save cropped image as an jpg file
        # to passed on the ft_load() function
        cropped.save("cropped.jpg")
        ft_load("cropped.jpg")
        display_first(np.array(cropped.convert("L")))

        transposed = transpose_img(cropped)
        print(f"New shape after Transpose: {transposed.size}")
        grayscaled = transposed.convert("L")
        print(np.array(grayscaled))

        plt.imshow(grayscaled, cmap='gray')
        plt.axis('on')
        plt.show()
        os.remove("cropped.jpg")

    except Exception as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print(f"KeyboardInterrupt")
        return None


if __name__ == "__main__":
    main()
