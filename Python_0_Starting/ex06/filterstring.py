import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            if not isinstance(sys.argv[1], str):
                raise AssertionError("the arguments are bad")
            if not isinstance(int(sys.argv[2]), int):
                raise AssertionError("the arguments are bad")
            S = sys.argv[1]
            N = int(sys.argv[2])
            # split() will seperate string S
            # by delimiting space by default
            filtered = list(ft_filter(lambda w: len(w) > N, S.split()))
            print(filtered)
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as a:
        print(f"AssertionError: {a}")


if __name__ == "__main__":
    main()
