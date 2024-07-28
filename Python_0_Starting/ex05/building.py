import sys


def count_uppercase(str):
    """
    Count the number of uppercases in a string.

    Args:
        str: The input string.

    Returns:
        int: The number of uppercases in the string.
    """
    count = 0
    for c in str:
        if c.isupper():
            count += 1
    return count


def count_lowercase(str):
    """
    Count the number of lowercases in a string.

    Args:
        str: The input string.

    Returns:
        int: The number of lowercases in the string.
    """
    count = 0
    for c in str:
        if c.islower():
            count += 1
    return count


def count_punctuation(str):
    """
    Count the number of punctuations in a string.

    Args:
        str: The input string.

    Returns:
        int: The number of punctuations in the string.
    """
    count = 0
    for c in str:
        if c in '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            count += 1
    return count


def count_digit(str):
    """
    Count the number of digits in a string.

    Args:
        str: The input string.

    Returns:
        int: The number of digits in the string.
    """
    count = 0
    for c in str:
        if c.isdigit():
            count += 1
    return count


def display_str(argv):
    """
    Display informations of a string:
    - uppercases
    - lowercases
    - punctuations
    - spaces
    - digits
    """
    if len(argv) < 2:
        try:
            str_input = input("What is the text to count?\n")
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Ctrl+C")
        except EOFError:
            raise EOFError("Ctrl+D")
    else:
        str_input = argv[1]
    print(f"The text contains {len(str_input)} characters:")
    print(f"{count_uppercase(str_input)} upper letters")
    print(f"{count_lowercase(str_input)} lower letters")
    print(f"{count_punctuation(str_input)} punctuation marks")
    print(f"{str_input.count(' ')} spaces")
    print(f"{count_digit(str_input)} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            display_str(sys.argv)

    except AssertionError as a:
        print(f"AssertionError: {a}")
    except KeyboardInterrupt as k:
        print(f"\nKeyboardInterrupt: {k}")
    except EOFError as eof:
        print(f"EOFError: {eof}")


if __name__ == "__main__":
    main()
