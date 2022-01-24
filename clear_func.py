# This is a clear function
# https://www.geeksforgeeks.org/clear-screen-python/
# used this source

# import only system from os
from os import system, name


def clear():
    # logic for windows computers
    if name == 'nt':
        _ = system('cls')
    # for mac and linux()
    else:
        _ = system('clear')
