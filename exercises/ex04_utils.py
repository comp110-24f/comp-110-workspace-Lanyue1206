""""list Utility Functions"""

__author__ = "730679606"


def all(int_list: list[int], number: int) -> bool:
    """This function checks if all numbers match the indicated number."""

    index = 0  # prime the loop

    if len(int_list) == 0:  # return False the list is empty
        return False

    while index < len(int_list):  # Checking within the right range
        if number == int_list[index]:
            index += 1  # Keep checking all the numbers
        else:
            return False  # Return False if there is unmatched number
    return True  # Return True if all numbers are matched


def max(input: list[int]) -> int:
    """This function should return the largest number in the list."""

    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # If the list is empty, the function should result in a ValueError.

    max: int = input[0]  # Start weith the first number in the list
    index = 1  # Prime the loop

    while index < len(input):
        if input[index] > max:
            max = input[index]  # Update max_value if the current element is larger
        index += 1  # Keep moving to the next element
    return max  # Return the max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function checks if every element at every index is equal in both lists."""

    # Edge case: If lengths are different, return False
    if len(list1) != len(list2):
        return False  # Return False if two lists have different lengths.

    # Edge case: Check if both lists are empty
    if len(list1) == 0 and len(list2) == 0:
        return True  # Return True if two lists are empty.

    index = 0  # Prime the loop
    while index < len(list1):
        if list1[index] == list2[index]:
            index += 1  # Check the number in each index
        else:
            return False  # Return False if there is unmatched number.
    return True


def extend(a: list[int], b: list[int]) -> None:
    """This function edit the first list by appending values in the second list to the end of it."""

    index = 0  # Prime the loop

    while index < len(b):
        a.append(b[index])  # Append the values in b to a
        index += 1  # Keep adding the number
