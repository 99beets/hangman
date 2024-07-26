from countries import get_europe, get_asia, get_africa, get_americas, get_oceania
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
        europe = get_europe()
        return random.choice(europe)
        print(random.choice(europe))
    elif continent == 2:
        print("You have selected Asia.")
        asia = get_asia()
        # print(random.choice(asia))
    elif continent == 3:
        print("You have selected Africa.")
        africa = get_africa()
        # print(random.choice(africa))
    elif continent == 4:
        print("You have selected Americas.")
        americas = get_americas()
        # print(random.choice(americas))
    elif continent == 5:
        print("You have selected Oceania.")
        oceania = get_oceania()
        # print(random.choice(oceania))

    return "unknown"

