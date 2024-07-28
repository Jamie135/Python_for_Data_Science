import sys


def morse(text, morse_code):
    encoded = ""
    for c in text.upper():
        if c in morse_code:
            encoded += morse_code[c] + ' '
        else:
            raise AssertionError("the arguments are bad")
    # strip removes all leading and trailing spaces
    return encoded.strip()


def main():
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        encoded = morse(sys.argv[1], NESTED_MORSE)
        print(encoded)
    except AssertionError as a:
        print(f"AssertionError: {a}")


if __name__ == "__main__":
    main()
