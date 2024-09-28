"""Practice of importing functions from different files."""

__author__ = "730679606"


def concat(word1: str, word2: str) -> str:
    concatenation = word1 + word2
    return concatenation


if "__name__" == "__main__":
    word1 = "happy"
    word2 = "tuesday"
    print(concat(word1="happy", word2="tuesday"))
