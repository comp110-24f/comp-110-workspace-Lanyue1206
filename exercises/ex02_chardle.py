"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730679606"


# Gather a input of word from the user.
def input_word() -> str:
    word = str(input("Enter a 5-character word: "))

    # Check if the word only has 5 chracters.
    # If not, print error message and exit the program early.
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


# Gather a input of letter from the user.
def input_letter() -> str:
    letter = str(input("Enter a single character: "))

    # Check if the letter only has single chracter.
    # If not, print error message and exit the program early.
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    # Tell the user the begining of the searching progress.
    print("Searching for", letter, "in", word)
    # Initialize the count number to 0.
    count = 0

    # Use if to check indices of matches
    if letter == word[0]:
        # Print the message to notic the user if the letter is found at this index.
        print(letter, "found at index 0")
        # If the condition is true, the count number will increase 1.
        count += 1
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

    # Print the number of instances found in word if the count number >= 1
    if count >= 1:
        print(count, "instances of", letter, "found in", word)

    # Print the notice of no instances found
    # when input letter is not matched with any letters in the word.
    if (
        letter != word[0]
        and letter != word[1]
        and letter != word[2]
        and letter != word[3]
        and letter != word[4]
    ):
        print("No instances of", letter, "found in", word)


# Define the main function that calls the functions I just defined.
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
