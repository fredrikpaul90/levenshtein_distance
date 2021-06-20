import csv

import pandas as pd

from levenshtein_distance import levenshtein_distance


def get_levenshtein_matches(data: pd.DataFrame, levenshtein_dist: int) -> list:
    """
    Function that returns a unique list of words with
    Levenshtein Distance = `levenshtein_dist`.

    Parameters
    ----------
    data : pd.DataFrame
        Table that contains at least columns `HUNDENAME` and `distance`.
    levenshtein_dist : int
        The word to compare against word1.

    Returns
    -------
    list
        List of unique dog names with Levenshtein Distance = `levenshtein_dist`.
    """
    data = data[data["distance"] == levenshtein_dist]

    return list(data["HUNDENAME"].drop_duplicates())


def main():
    # Data can be downloaded directly from its source with:
    # data = pd.read_csv("https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv")

    # Read in data if it's stored under /levenshtein/data
    data = pd.read_csv("data/20210103_hundenamen.csv")

    # The word to match
    comparison_word = "Luca"

    # Create new column that contains the levenshtein distance between
    # comparison_word and the dog name in data["HUNDENAME]
    data["distance"] = data.apply(
        lambda row: levenshtein_distance(comparison_word, row["HUNDENAME"]),
        axis=1
    )

    # Output unique names with levenshtein_distance == 1
    names = get_levenshtein_matches(data, levenshtein_dist=1)

    # Write unique dog names with distance == 1 to csv
    with open("output/names.csv", "w") as f:
        write = csv.writer(f)
        write.writerow(names)


if __name__ == '__main__':
    main()
