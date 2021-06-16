import numpy as np
import pandas as pd
import os

from functions.displayMenu import *
from functions.beamDeflection import beamDeflection
from functions.beamSuperposition import beamSuperposition
from functions.beamPlot import beamPlot
from functions.dataLoad import dataLoad

# Main script

# can only run one beam at a time

# Initial conditions
df = pd.DataFrame({"loadPosition": [],
                   "forceVal": []})
beamLength = 0
beamLength = 10
beamSupport = "both"

print('Initial 10 meter beam of support-type "both" loaded ')

while True:
    menuItems = np.array(["Configure beam", "Configure loads",
                          "Save beam and loads", "Load beam and loads", "Generate plot", "Quit"])
    mainChoice = displayMenu(menuItems)

    if mainChoice == 1:  # Configure beam
        while True:
            try:
                beamLength = float(input("Please enter the length of beam in meters: "))

                if beamLength <= 0:
                    raise
                supportItems = np.array(["both", "cantilever"])
                supportChoice = displayMenu(supportItems)
                if supportChoice == 1:
                    beamSupport = "both"
                elif supportChoice == 2:
                    beamSupport = "cantilever"
                break
            except:
                print("Beam must be a positive value. Please try again")

        print("Beam loaded")
        # first row of dataframe is reserved for beam information

    if mainChoice == 2:  # Configure loads
        while True:
            loadItems = np.array(["See current loads", "Add a load",
                                  "Remove a load", "Go to main menu"])
            print("What do you wish to do?")
            loadChoice = displayMenu(loadItems)

            if loadChoice == 1:  # See current loads
                if sum(df.loadPosition) == 0:
                    print("There are currently no load forces on the beam.")
                    pass
                else:
                    print("The current loads and forces are: \n")

                    temp = {'': [], 'Forces [N]': [], 'Positions [m]': []}
                    weights = pd.DataFrame(data=temp)
                    lPositions = np.array(df.loadPosition)
                    fVal = np.array(df.forceVal)

                    for i in range(np.size(lPositions)):
                        weights = weights.append(
                            {'': 'W{}'.format(i + 1), 'Forces [N]': fVal[i], 'Positions [m]': lPositions[i]}, ignore_index=True)

                    print(weights.to_string(index=False), '\n')

            if loadChoice == 2:  # Add a load
                while True:
                    try:
                        load_pos = float(inputNumber(
                            "Enter position of load in meters (beam is {} meters): ".format(beamLength)))

                        if load_pos < 0 or load_pos > beamLength:  # must not be longer than length of beam
                            raise
                        # load position and load force is appended to df
                        force_val = float(inputNumber("Enter the force at the position: "))
                        df = df.append({"loadPosition": load_pos,
                                        "forceVal": force_val}, ignore_index=True)
                        break
                    except:
                        print("Your load position can not be out of range of the beam")

            if loadChoice == 3:  # Remove a load
                # prints dataframe and the user can select which line to remove
                while True:
                    try:
                        print("The forces are: \n")
                        temp = {'': [], 'Forces [N]': [], 'Positions [m]': []}
                        weights = pd.DataFrame(data=temp)
                        lPositions = np.array(df.loadPosition)
                        fVal = np.array(df.forceVal)

                        for i in range(np.size(lPositions)):
                            weights = weights.append(
                                {'': 'W{}'.format(
                                    i + 1), 'Forces [N]': fVal[i], 'Positions [m]': lPositions[i]},
                                ignore_index=True)

                        print(weights.to_string(index=False), '\n')

                        removed_forces = inputString(
                            'Please enter a comma seperated list of the forces you wish to remove, e.g. "W1,W2" ', 'wW1234, ')

                        removed_forces

                        if len(df.loadPosition) == 0:
                            raise
                        break
                    except:
                        print("There are currently no load forces on the beam")

            if loadChoice == 4:  # Go to main menu
                break

    if mainChoice == 3:  # Save beam and loads
        while True:
            try:
                saving_filename = input("What do you wish to name your file ?: ")

                if os.path.isfile(saving_filename + ".csv"):
                    raise
                df_for_saving = df.insert(2, "beamLength", [beamLength], True)
                df_for_saving = df.insert(3, "beamSupport", [beamSupport], True)

                # file shall not overwrite old file
                s = df.to_csv(index=False)
                f = open(saving_filename + ".csv", "w")  # write
                f.write(s)
                f.close()
                cwd = os.getcwd()
                print('file saved as "{}" in "{}"'.format(saving_filename, cwd))

                break
            except:
                print("File already exists. Please enter another filename")

    if mainChoice == 4:  # Load beam and loads
        load_filename = input("Please enter the csv file you wish to load")

        dataLoad(load_filenamefilename)

        # use dataload funktion

        print("Data loaded")

        "cantilever"
    if mainChoice == 5:  # Generate plot
        beamPlot(beamLength, np.array(df.loadPosition), np.array(df.forceVal), beamSupport)

        # beamPlot(beamLength, ) runs here
        # ekstra plot function ?
        # print list of current forces in console

        print("Beam plot created succesfully")

    if mainChoice == 6:  # exits program
        print("Program closed")
        break
