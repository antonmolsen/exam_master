import numpy as np


def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass

    return num


def displayMenu(options):

    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while True:
        try:
            choice = inputNumber("Please choose a menu item: ")
            if(choice == 0):
                break
            elif(not(np.any(choice == np.arange(len(options))+1))):
                raise
            break

        except:
            print('Please those a number from the list')

    return choice
