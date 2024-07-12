def menu():

    while True:
        try:
            continent = int(input("Select a region:\n 1. Europe\n 2. Asia\n 3. Africa\n 4. Americas\n 5. Oceania\n"))
            if continent <= 1 and continent <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Not a valid number.")


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