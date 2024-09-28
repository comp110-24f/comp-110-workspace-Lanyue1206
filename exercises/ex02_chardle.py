"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730679606"


def input_word() -> str:
    """This function gathers an input of word from the user."""
    word = str(input("Enter a 5-character word: "))
    if len(word) != 5:  # Check if the word only has 5 characters.
        print(
            "Error: Word must contain 5 characters."
        )  # If not, print error message and exit the program early.
        exit()
    else:
        return word


def input_letter() -> str:
    """This function gathers an input of letter from the user"""
    letter = str(input("Enter a single character: "))

    if len(letter) != 1:  # Check if the letter only has single character.
        print(
            "Error: Character must be a single character."
        )  # If not, print error message and exit the program early.
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    """This function checks if the letter is contained in the word."""
    print(
        "Searching for", letter, "in", word
    )  # Tell the user the beginning of the searching progress.

    count = 0  # Initialize the count number to 0.

    if letter == word[0]:  # Check indices of matches
        print(
            letter, "found at index 0"
        )  # Print the message to notice the user if the letter is found at this index.
        count += 1  # If the condition is true, the count number will increase 1.
    # Repeat searching for the rest of four indices.
    if letter == word[1]:
        print(letter, "found at index 1")
        count += 1
    if letter == word[2]:
        print(letter, "found at index 2")
        count += 1
    if letter == word[3]:
        print(letter, "found at index 3")
        count += 1
    if letter == word[4]:
        print(letter, "found at index 4")
        count += 1

    # Check if no instances were found
    if count == 0:
        print(
            "No instances of", letter, "found in", word
        )  # Print the notice of no instances found if the count number = 0
    elif (
        count == 1
    ):  # Print the number of instances found in word if the count number >= 1
        print(count, "instance of", letter, "found in", word)  # The output is singular
    else:
        print(count, "instances of", letter, "found in", word)  # The output is plural


def main() -> None:
    """The main function calls the functions I just defined."""
    contains_char(word=input_word(), letter=input_letter())


# Call the main function.
if __name__ == "__main__":
    main()
