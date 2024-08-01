import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def convert_pop(pop):
    """Converts population string into a numeric value"""
    if pop.endswith("M"):
        return float(pop[:-1]) * 1e6
    elif pop.endswith("k"):
        return float(pop[:-1]) * 1e3
    else:
        return float(pop)


def main():
    """Loads the file population_total.csv,
    and displays the country information of your campus
    versus other country of your choice"""
    try:
        df = load("../resources/population_total.csv")
        if not isinstance(df, pd.DataFrame):
            raise Exception("loaded content is not a dataframe")

        # iloc[:, 1:] allow us to selecs data using indexes
        # ":" means all rows, "1:" means all columns starting from colum 1
        france = df[df['country'] == 'France'].iloc[:, 1:]
        thailand = df[df['country'] == 'Thailand'].iloc[:, 1:]
        print(f"france:\n{france}")
        print(f"thailand:\n{thailand}")

        years = france.columns.astype(int)
        print(f"years:\n{years}")

        # flatten() converts a DataFrame into a one-dimensional array
        fr_pop = france.values.flatten()
        th_pop = thailand.values.flatten()

        fr_pop = [convert_pop(pop) for pop in fr_pop]
        th_pop = [convert_pop(pop) for pop in th_pop]

        plt.plot(years, fr_pop, label='France', color='green')
        plt.plot(years, th_pop, label='Thailand', color='blue')

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')

        # set the limit and range to display the x axis
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1800, 2040)

        # set the format to display the y axis
        max_pop = max(max(fr_pop), max(th_pop))
        y_ticks = [pop * 1e7 for pop in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        return None
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        return None


if __name__ == "__main__":
    main()
