def tries():
    tries += 1
    if tries == 1:
        print("/\n")
        print("Try again.\n")
    else:
        if tries == 2:
            print("/ \\\n")
            print("Try again.\n")
        else:
            if tries == 3:
                print(" |")
                print("/ \\\n")
                print("Try again.\n")
            else:
                if tries == 4:
                    print("-|")
                    print("/ \\\n")
                    print("Try again.\n")
                else:
                    if tries == 5:
                        print("-|-")
                        print("/ \\\n")
                        print("Try again.\n")
                    elif tries == 6:
                        print(" O")
                        print("-|-")
                        print("/ \\")
                        print("Sorry, you lost.\n")


# if len(letter) != 1:
#   print("Invalid input. Please enter only one letter.")
#  continue

for letter in answer:
    if letter in all_guessed_letters:
        output.append(letter)
    else:
        output.append('_')