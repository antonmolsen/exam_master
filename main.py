import numpy as np
import pandas as pd
import os

from functions.displayMenu import *
from functions.beamDeflection import beamDeflection
from functions.beamSuperposition import beamSuperposition
from functions.beamPlot import beamPlot
from functions.dataLoad import dataLoad
from functions.dataRemove import dataRemove

# Main script #

# Main script for calculations and plots of beam deflection. The user is able to configure a
# new beam if she wishes. The user can also load/save data (as csv). If read data is erroneous
# the program will read the correct data, and remove the erroneous parts. The program can only
# run one beam at a time, and will tell the user if she has loads out of bounds of the new beam.

# Initial conditions
df = pd.DataFrame({"loadPosition": [],"forceVal": []})
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
                init_beam_sup = beamSupport
                init_beam_len = beamLength

                beamLength = float(input("Please enter the length of beam in meters: "))
                if beamLength <= 0:
                    raise
                supportItems = np.array(["both", "cantilever"])
                supportChoice = displayMenu(supportItems)
                if supportChoice == 1:
                    beamSupport = "both"
                elif supportChoice == 2:
                    beamSupport = "cantilever"


                if np.array(beamLength < df.loadPosition).any() == True:
                    ans = inputString(
                        "Your new beam is shorter than some of the current load positions. \nDo you wish to enter your new beam, and therefore remove the loads that are out of bounds? y/n?: ", "yn")
                    if ans == "y":  # yes - we remove loads above new length
                        df_bool = df.loadPosition > beamLength
                        removal_indexes = df.index.values[df_bool]
                        df = dataRemove(df, removal_indexes)

                    elif ans == "n":  # no - go back to main menu
                        beamLength = init_beam_len
                        beamSupport = init_beam_sup
                        print("Going back to main menu")
                        break

                break
            except:
                print("Beam must be a positive value. Please try again")

        print("Beam loaded")
        # first row of dataframe is reserved for beam information

    if mainChoice == 2:  # Configure loads
        while True:
            loadItems = np.array(["See current loads", "Add a load",
                                  "Remove a load", "Remove all loads", "Go to main menu"])
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
                        if len(df.loadPosition) == 0:
                            raise

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

                        # removal of forces from string input
                        removed_forces = inputString(
                            'Please enter a list of the forces you wish to remove, e.g. "W1,W2" (enter nothing to go back): ', 'wW1234567890, ')
                        removed_forces = np.fromstring(
                            removed_forces.upper().replace("W", ""), dtype=int, sep=',')

                        df = dataRemove(df, removed_forces)

                        break
                    except:
                        print("There are currently no load forces on the beam.")
                        break

            if loadChoice == 4:  # remove all loads
                df = df.iloc[0:0]    
                # df.loadPosition = 0
                # df.forceVal = 0
                print("All loads removed succesfully")

            if loadChoice == 5:  # Go to main menu
                break

    if mainChoice == 3:  # Save beam and loads
        while True:
            try:
                saving_filename = input("What do you wish to name your file ?: ")
                df_for_saving = df
                # if file exists the user should rename the file
                if os.path.isfile(saving_filename + ".csv"):
                    raise
                df_for_saving.insert(2, "beamLength", np.nan, False)
                df_for_saving.insert(3, "beamSupport", '', False)

                df_for_saving.at[0, "beamLength"] = beamLength
                df_for_saving.at[0, "beamSupport"] = beamSupport

                # file shall not overwrite old file
                s = df_for_saving.to_csv(index=False)
                f = open(saving_filename + ".csv", "w")  # write
                f.write(s)
                f.close()
                cwd = os.getcwd()
                print('File saved as "{}" in "{}"'.format(saving_filename + ".csv", cwd))

                break
            except:
                print("File already exists. Please enter another filename")

    if mainChoice == 4:  # Load beam and loads
        files = np.array(os.listdir(os.getcwd()))
        files = files[np.char.find(files, '.csv') > 0]
        nExit = np.size(files)
        files = np.hstack((files, 'Exit'))
        print('These files are availble in the current working directory:')
        fileChoice = displayMenu(files) - 1

        if fileChoice == nExit:
            pass

        else:
            filename = files[int(fileChoice)]

            df, beamLength, beamSupport = dataLoad(filename)

            print("Data loaded")

    if mainChoice == 5:  # Generate plot
        beamPlot(beamLength, np.array(df.loadPosition), np.array(df.forceVal), beamSupport)

        # beamPlot(beamLength, ) runs here
        # ekstra plot function ?
        # print list of current forces in console

        print("Beam plot created succesfully")

    if mainChoice == 6:  # exits program
        print("Program closed")
        break
