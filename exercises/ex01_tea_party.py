""""A program to plan a tea party."""

__author__: str = "730679606"


def main_planner(guests: int) -> None:
    """Entrypoint of the program"""

    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# make a function call to the subprogram
# print the calculated value with a string literal to describe the result
# makes sure use the correct variable to call the function definition


def tea_bags(people: int) -> int:
    """Calculate the quantity of tea bags based on the number of guests."""
    return people * 2


# make sure return value aligns with the content, which is two tea bags per person.


def treats(people: int) -> int:
    """Calculate the number of treats based on the number of guests."""
    return int(1.5 * tea_bags(people=people))


# make sure the type of return value is integer.
# use keyword argument to make a call to tea_bags function
# use that value to compute the number of treats.


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and the treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


# Calculate the total cost by adding two costs together
# the unit cost of teas is 0.5 and unit cost of treats is 0.75.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
# ask user for the number of guests and calling "main_planner"
