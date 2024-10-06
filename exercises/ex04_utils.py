""""list Utility Functions"""

__author__ = "730679606"


def all(int_list: list[int], number: int) -> bool:
    index = 0
    if len(int_list) == 0:
        return False
    while index < len(int_list):
        if number == int_list[index]:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max: int = input[0]
    index = 1  # Prime the loop

    while index < len(input):
        if input[index] > max:
            max = input[index]
        index += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    index = 0

    if len(list1) != len(list2):
        return False

    if len(list1) == 0 or len(list2) == 0:
        return False

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
