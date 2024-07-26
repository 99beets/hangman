from menu import menu
import random


def check_letter(char=""):

    answer = menu()
    placeholder = ["_" if char.isalpha() else char for char in answer]  # Add underscore placeholder for unknown letter
    wrong_guess = 0  # Wrong attempts counter
    entered_letters = set()  # Store already entered letters

    print("Answer:", " ".join(placeholder))
    correct_word = len(answer)

    while True:
        letter = input("Please enter a letter\n")  # .lower()
        if len(letter) != 1:  # Check if the input is a single letter
            print("Invalid input. Please enter only one letter.")
            continue

        if letter in answer:
            if letter in entered_letters:
                print("You have already entered this letter. Try a different one.\n")
            else:
                print("You have guessed correctly!\n")
                entered_letters.add(letter)

            for index, char in enumerate(answer):
                if char == letter.upper() or char == letter.lower():
                    placeholder[index] = letter

            print("Answer:", " ".join(placeholder))

        else:
            wrong_guess += 1

            if wrong_guess == 1:
                print("/\n")
                print("Try again.\n")
                print("Correct word:", " ".join(placeholder )+ "\n")

            else:
                if wrong_guess == 2:
                    print("/ \\\n")
                    print("Try again.\n")
                    print("Correct word:", " ".join(placeholder))
                else:
                    if wrong_guess == 3:
                        print(" |")
                        print("/ \\\n")
                        print("Try again.\n")
                        print("Correct word:", " ".join(placeholder))
                    else:
                        if wrong_guess == 4:
                            print("-|")
                            print("/ \\\n")
                            print("Try again.\n")
                            print("Correct word:", " ".join(placeholder))
                        else:
                            if wrong_guess == 5:
                                print("-|-")
                                print("/ \\\n")
                                print("Try again.\n")
                                print("Correct word:", " ".join(placeholder))
                            else:
                                if wrong_guess == 6:
                                    print(" O")
                                    print("-|-")
                                    print("/ \\")
                                    print("Sorry, you lost. The correct answer was: " + answer)
                                    break

    while True:
        replay = input("Do you want to play again?\n1. Yes\n2. No\n")
        if replay == "1":
            check_letter()
            break
        elif replay == "2":
            print("Good bye.")
            break
        else:
            print("Invalid input. Please choose 1 or 2.")


check_letter()
