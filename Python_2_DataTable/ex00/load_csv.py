import pandas as pd


def load(path: str) -> pd:
    """ This function takes a path as argument,
    writes the dimensions of the data set as an array and returns it"""
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df
    except Exception as e:
        print(f"Errors: {e}")
        return None
