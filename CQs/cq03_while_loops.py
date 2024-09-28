"""Practice with while loops."""

__author__ = "730679606"


def num_instances(phrase: str, search_char: str) -> None:
    # Create a local variable called count. Initiate its value to 0.
    count = 0
    index = 0
    while index <= len(phrase) - 1:
        if search_char == phrase[index]:
            count += 1
        index += 1
    print(count)
