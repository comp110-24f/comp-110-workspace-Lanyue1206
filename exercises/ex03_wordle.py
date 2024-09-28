""""Structured Wordle"""

__author__ = "730679606"


def input_guess(secret_word_length: int) -> str:
    """This function prompts the user to enter a word in correct length."""

    guess = str(input(f"Enter a {secret_word_length} character word:"))

    while len(guess) != secret_word_length:  # Check the word length
        guess = input(
            f"That wasn't {secret_word_length} chars! Try again:"
        )  # Keep asking until get a word in correct length
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This function checks indexes of the word to see if it matches the character."""
    """If a match is found, it returns True; otherwise, it returns False."""

    assert len(char_guess) == 1
    index = 0  # Initialize the index

    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """This function make the check results emojified."""
    assert len(guess) == len(secret)

    white_box: str = "\U00002B1C"  # Initialize the unicode of emoji.
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    emoji = ""  # Initialize the emojified line.
    index = 0  # Initialize the index value.

    while index < len(guess):
        if guess[index] == secret[index]:
            """A green box for the correct letter in the right position."""
            emoji += green_box
            index += 1  # Repeat to check for the next index
        elif contains_char(secret, guess[index]) is True:
            """A yellow box for the correct letter in the wrong position."""
            emoji += yellow_box
            index += 1
        elif contains_char(secret, guess[index]) is False:
            """A white box for the incorrect letter."""
            emoji += white_box
            index += 1
    return emoji  # Print the final result of emoji.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turn = 1  # Initialize the turn
    word_length = len(secret)
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")  # Format the game
        guess: str = input_guess(word_length)  # Ask input for the correct length
        print(emojified(guess, secret))  # Emojifies the input
        if guess == secret:
            print(f"You won in {turn}/6 turns!")  # Display the victory message.
            return None
        turn += 1  # Keep asking the user to enter a word until get the correct answer

    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")  # End the game after 6 turns.
        return None


if __name__ == "__main__":
    main(secret="codes")
