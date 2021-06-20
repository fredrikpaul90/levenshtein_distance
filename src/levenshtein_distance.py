import numpy as np


def levenshtein_distance(word1: str, word2: str) -> int:
    """
    Function that returns the Levenshtein Distance between two words.

    Parameters
    ----------
    word1 : str
        The word to compare against word2.
    word2 : str
        The word to compare against word1.

    Returns
    -------
    int
        The Levenshtein Distance between word1 and word2.
    """
    length_word1 = len(word1)
    length_word2 = len(word2)

    distances = np.zeros((length_word1 + 1, length_word2 + 1))
    distances[:, 0] = range(length_word1 + 1)
    distances[0] = range(length_word2 + 1)

    for w1 in range(1, length_word1 + 1):
        for w2 in range(1, length_word2 + 1):
            if word1[w1 - 1] == word2[w2 - 1]:
                distances[w1][w2] = distances[w1 - 1][w2 - 1]
            else:
                a = distances[w1][w2 - 1]
                b = distances[w1 - 1][w2]
                c = distances[w1 - 1][w2 - 1]

                if a <= b and a <= c:
                    distances[w1][w2] = a + 1
                elif b <= a and b <= c:
                    distances[w1][w2] = b + 1
                else:
                    distances[w1][w2] = c + 1

    return int(distances[length_word1][length_word2])
