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


def main():
    """
    This function serves as the main entry point of the script.
    It loads animal.jpeg, performs various image processing
    operations, and displays the resulting images. The script supports
    cropping, grayscale conversion, and zoomed image display. Errors related
    to file format and existence are caught and displayed.
    """
    try:
        path = "../resources/animal.jpeg"
        image = Image.open(path)
        if image is None:
            raise AssertionError("failed to load image.")

        print(ft_load(path))

        zoomed = image.crop((400, 200, 800, 600))
        npzoomed = np.array(zoomed)

        print(f"New shape after slicing: "
              f"({npzoomed.shape[0]}, {npzoomed.shape[1]})")

        # L" signifie "Luminance", ce qui signifie que
        # l'image résultante n'aura qu'un seul canal,
        # représentant la luminosité de chaque pixel
        grayscaled = zoomed.convert("L")
        display_first(np.array(grayscaled))

        # gray indique que la carte de couleurs à utiliser
        # pour afficher les données de l'image est en niveaux de gris
        plt.imshow(grayscaled, cmap='gray')
        plt.axis('on')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
