""""list Utility Functions"""

__author__ = "730679606"


def all(int_list: list[int], number: int) -> bool:
    index = 0

    while index < len(int_list):
        if number == int_list[index]:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    index = 0  # Prime the loop

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    while index < len(input):
        if input[index] < input[index + 1]:
            return input[index + 1]
        else:
            return input[index]
    index += 1


def is_equal(list1: list[int], list2: list[int]) -> bool:
    index = 0

    while index < len(list1):
        if list1[index] == list2[index]:
            index += 1
        else:
            return False
    return True


def extend(a: list[int], b: list[int]) -> None:
    index = 0

    while index < len(b):
        a.append(b[index])
        index += 1
