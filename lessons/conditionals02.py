def should_i_eat(hungry: bool) -> None:
    """Tells me whether or nor to eat based on hunger."""
    if hungry:  # conditional/ bollen expression
        print("Eat some food silly goose!")  # 'then' block
    else:
        print("Do your Comp 110 homework instead.")  # 'else' block
    print("I'm proud of you.")  # either way, be kind to yourself


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"

    else:
        return "no match!"


print((check_first_letter(word="happy", letter="h")))
# if there is no print, no value is shown
