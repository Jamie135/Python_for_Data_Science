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
        years = france.columns[1:].astype(int)
        expectancy = france.values[0][1:]

        plt.figure(figsize=(10, 6))
        plt.plot(years, expectancy, label='Life Expectancy', color='blue')
        plt.title('France Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        return None


if __name__ == "__main__":
    main()
