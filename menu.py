from countries import europe, asia, africa, americas, oceania
import random
def menu():

    while True:
        try:
            continent = int(input("Select a region:\n 1. Europe\n 2. Asia\n 3. Africa\n 4. Americas\n 5. Oceania\n"))
            if continent > 0 and continent < 6:
                break
            else:
                print("Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Not a valid number.")


    if continent == 1:
        print("You have selected Europe.")
        print(random.choice(europe))
    elif continent == 2:
        print("You have selected Asia.")
    elif continent == 3:
        print("You have selected Africa.")
    elif continent == 4:
        print("You have selected Americas.")
    elif continent == 5:
        print("You have selected Oceania.")

menu()