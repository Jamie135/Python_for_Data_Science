import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        try:
            argInt = int(sys.argv[1])
            if argInt % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except IndexError:
            pass
        except ValueError:
            raise AssertionError("argument is not an integer")

    except AssertionError as a:
        print(f"AssertionError: {a}")
