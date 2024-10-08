import sys


def word_to_dict(word):
    """This function converts a string to a dictionary: key = letter,
    value = list of indexes where letter is found"""
    word_dict = {}
    for count, letter in enumerate(word):
        if letter in word_dict:
            word_dict[letter].append(count)
        else:
            word_dict[letter] = [count]
    return word_dict


def check_guess(letter, letters_pending, letters_found):
    """This function checks to see if user guess the correct letter"""

    # correct guess
    if letter in letters_pending:
        letter_index = letters_pending[letter].pop(0)  # return first letter's index
        letters_found.add(letter_index)

        # check if list is empty
        if len(letters_pending[letter]) == 0:
            del letters_pending[letter]

        return True

    return False


def display_word_status(word, indexes_found):
    """This function displays the letters that user found and underscores for letters remain to be found"""
    status = []
    for i in range(len(word)):
        if i in indexes_found:
            status.append(word[i])
        else:
            status.append('_')
    print('\n[', " ".join(status), '] \n')


def main():
    try:
        print("Welcome to Hangman Game!\n")
        word = input("Please enter a word: ").lower()

        # check if word input is valid
        while not word.isalpha():
            word = input("Please enter a valid word: ").lower()

        letters_pending = word_to_dict(word)  # a dict with key: letter, value: list of indexes where letter is found
        indexes_found = set()  # a set with all letter indexes found by user

        tries = 6
        while tries > 0:
            display_word_status(word, indexes_found)
            print(f"You have {tries} tries!")
            letter = input("Guess a letter: ")

            # check if letter input is valid
            while (not letter.isalpha()) or len(letter) > 1:
                letter = input("Guess a valid letter: ")

            if check_guess(letter, letters_pending, indexes_found):
                print("\nYou found a letter!")
            else:
                print("\nIncorrect letter. Try again!")
                tries -= 1

            # empty dict means we found all letters
            if not letters_pending:
                print("Congratulations, you won!")
                break

        if tries == 0:
            print("You lost, better luck next time...")

    except KeyboardInterrupt:
        print("\nGame is stopping... Goodbye")
        sys.exit()


if __name__ == "__main__":
    main()