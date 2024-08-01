import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files then visualizes
    the correlation between GNP and life expectancy
    through a scatter plot for the year 1900."""
    try:
        file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        df_gnp = load(f"../resources/{file}")
        df_expectancy = load("../resources/life_expectancy_years.csv")
        if not isinstance(df_gnp, pd.DataFrame)\
                or not isinstance(df_expectancy, pd.DataFrame):
            raise Exception("loaded content is not a dataframe")

        gnp = df_gnp['1900']
        expectancy = df_expectancy['1900']

        plt.scatter(gnp, expectancy)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        return None


if __name__ == "__main__":
    main()
