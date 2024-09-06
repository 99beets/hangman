import random

import awoc

# Initialize the AWOC class.
my_world = awoc.AWOC()


def get_europe():
    # Retrieve the full list of countries of Europe.
    europe = my_world.get_countries_list_of('Europe')

    europe_indices_to_delete = [46, 24, 22, 18, 16]

    # Reversing the indices order to avoid ordering issues
    for index in sorted(europe_indices_to_delete, reverse=True):
        del europe[index]

    # Print the list of countries with their indices.
    # for index, country in enumerate(europe):
    #  print(f"{index}. {country}")

    return europe


def get_asia():
    asia = my_world.get_countries_list_of('Asia')

    asia_indices_to_delete = [26, 13, 11, 10, 6]

    for index in sorted(asia_indices_to_delete, reverse=True):
        del asia[index]

    # for index, country in enumerate(europe):
    # print(f"{index}. {country}")

    return asia


def get_africa():
    africa = my_world.get_countries_list_of('Africa')

    africa_indices_to_delete = [55, 41, 39, 32]

    for index in sorted(africa_indices_to_delete, reverse=True):
        del africa[index]

    # for index, country in enumerate(africa):
    # print(f"{index}. {country}")

    return africa


def get_americas():
    north_america = my_world.get_countries_list_of('North America')
    south_america = my_world.get_countries_list_of('South America')

    americas = north_america + south_america

    americas_indices_to_delete = [45, 37, 32, 28, 24, 23]

    for index in sorted(americas_indices_to_delete, reverse=True):
        del americas[index]

    # for index, country in enumerate(americas):
    # print(f"{index}. {country}")

    return americas

def get_oceania():
    oceania = my_world.get_countries_list_of('Oceania')

    # Country indices to be deleted from Oceania
    oceania_indices_to_delete = [24, 17, 14, 13, 12, 11, 6, 5, 3, 2]

    # Delete countries from Oceania
    for index in sorted(oceania_indices_to_delete, reverse=True):
        del oceania[index]

    # for index, country in enumerate(oceania):
    #  print(f"{index}. {country}")

    return oceania
