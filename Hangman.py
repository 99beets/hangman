from check_letter import check_letter
from menu import menu


def menu():
    while True:
        try:
            continent = int(input(
                "Select a region:\n 1. Europe\n 2. Asia\n 3. Africa\n 4. Americas\n 5. Oceania\nPlease enter a number between 1 and 5: "))
            if 1 <= continent <= 5:
                break  # Exit the loop if the input is valid
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("The input provided is not a valid number.")

    if continent == 1:
        print("You have selected Europe.")
    elif continent == 2:
        print("You have selected Asia.")
    elif continent == 3:
        print("You have selected Africa.")
    elif continent == 4:
        print("You have selected Americas.")
    elif continent == 5:
        print("You have selected Oceania.")


menu()









