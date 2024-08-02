import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Loads the file life_expectancy_years.csv,
    and displays the country information of your campus"""
    try:
        df = load("../resources/life_expectancy_years.csv")
        if not isinstance(df, pd.DataFrame):
            raise Exception("loaded content is not a dataframe")
        # filter the DataFrame to year
        # syntax: france is equal to SELECT 'country'
        # WHERE country == 'France'
        france = df[df['country'] == 'France']
        print(f"france:\n{france}")

        # retreive all the years column starting from index 1
        # index 0 corresponds to country column
        years = france.columns[1:].astype(int)
        print(f"years:\n{years}")

        # retreive all france's data from the first row values[0]
        expectancy = france.values[0][1:]
        print(f"expectency:\n{expectancy}")

        plt.plot(years, expectancy, label='Life Expectancy', color='blue')
        plt.title('France Life Expectancy Projections')
        plt.xticks(range(1800, 2100, 40), range(1800, 2100, 40))
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        return None


if __name__ == "__main__":
    main()
