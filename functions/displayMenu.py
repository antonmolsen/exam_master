import numpy as np

def inputNumber(prompt):
    # The function takes a prompt as input and forces the user to write a 
    # number. The function the returns that number

    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

def displayMenu(options):
    # The function has the menu items as a numpy array as input. It displays
    # the options and makes the user choose one of them. If the user inputs 0
    # it exits the menu. The function returns the number if thechosen menu item.

    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))

    choice = 0
    while True:
        try:
            choice = inputNumber("Please choose a menu item: ")
            if(choice == 0):
                break
            elif(not(np.any(choice == np.arange(len(options)) + 1))):
                raise
            break

        except:
            print('Please chose a number from the list: ')

    return choice

def inputString(prompt, acceptable):
    # The function takes a prompt and a string of acceptable characters and
    # checks if the user input is acceptable. The function return the accepted
    # string.

    while True:
        try:
            choice = input(prompt)
            for i in choice:
                if not(i in acceptable):
                    raise
            break
        except:
            print('Please only write numbers from the list \n')
    return choice
