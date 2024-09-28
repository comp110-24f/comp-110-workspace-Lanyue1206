"""Practice with conditonals, local variables, and user input."""

__author__ = "730679606"


def guess_a_number() -> None:
    secret = int(7)
    x = int(input("Guess a number: "))
    print("Your guess was", x)
    if secret == x:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
