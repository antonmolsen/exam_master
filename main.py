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

# Custom errors
class Error(Exception):
    # Base for other custom errors
    pass

class ValueOutOfBound(Error):
    # Error for when a value is out of bounds
    pass

class EmptyDF(Error):
    # Error when the user tries to work with / display a empty DataFrame
    pass

class FileOverwriteError(Error):
    # Error when the user tries to overwrite a already existing file
    pass


# Initial conditions
df = pd.DataFrame({"loadPosition": [],"forceVal": []})
beamLength = 10
beamSupport = "both"

while True:
    print('\nCurrent beam is {} meters of support type "{}"'.format(beamLength,beamSupport))

    menuItems = np.array(["Configure beam", "Configure loads",
                          "Save beam and loads", "Load beam and loads", "Generate plot", "Quit"])
    mainChoice = displayMenu(menuItems)
    
    if mainChoice == 1:  # Configure beam
        init_beam_sup = beamSupport
        init_beam_len = beamLength
        while True:
            try:
                beamLength = float(input("Please enter the length of beam in meters: "))
                if beamLength <= 0:
                    raise ValueOutOfBound("Beam must be a positive value")

                supportItems = np.array(["both", "cantilever"])
                supportChoice = displayMenu(supportItems)
                if supportChoice == 1:
                    beamSupport = "both"
                elif supportChoice == 2:
                    beamSupport = "cantilever"

                if np.array(beamLength < df.loadPosition).any():
                    ans = inputString(
                        "Your new beam is shorter than some of the current load positions. \nDo you wish to enter your new beam, and therefore remove the loads that are out of bounds? y/n?: ", "yn")
                    if ans == "y":  # yes - we remove loads above new length
                        df_bool = df.loadPosition > beamLength
                        removal_indexes = df.index.values[df_bool] +1
                        df = dataRemove(df, removal_indexes)
                        break

                    elif ans == "n":  # no - go back to main menu
                        beamLength = init_beam_len
                        beamSupport = init_beam_sup
                        print("Going back to main menu.")
                        break

                break
            except ValueOutOfBound as error:
                print(error)

            except ValueError:
                print('Please enter a valid number')

        print("Beam loaded")
        # first row of dataframe is reserved for beam information

    if mainChoice == 2:  # Configure loads
        while True:

            print('\nCurrent beam is {} meters of support type "{}"'.format(beamLength, beamSupport))

            loadItems = np.array(["See current loads", "Add a load",
                                  "Choose loads to remove", "Remove all loads", "Go to main menu"])
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
                            raise ValueOutOfBound('Your load position can not be out of range of the beam.')

                        force_val = float(inputNumber("Enter the force at the position: "))
                        if force_val < 0:  # force must not be negative, since we do
                            # not know if the given formulas are valid in that case.
                            raise ValueOutOfBound('Your force must be positive.')

                        df = df.append({"loadPosition": load_pos,
                                        "forceVal": force_val}, ignore_index=True)
                        break
                    except ValueOutOfBound as error:
                        print(error)

            if loadChoice == 3:  # Remove a load
                # prints dataframe and the user can select which line to remove
                while True:
                    try:
                        if len(df.loadPosition) == 0:
                            raise EmptyDF("There are currently no load forces on the beam.")

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

                        removed_forces = np.fromstring(removed_forces.upper().replace("W", ""), dtype=int, sep=',')

                        if np.any(removed_forces < 1) or np.any(removed_forces > np.size(lPositions)):
                            raise ValueOutOfBound('Please only choose loads from the list.')

                        df = dataRemove(df, removed_forces)

                        break
                    except ValueOutOfBound as error:
                        print(error)

                    except EmptyDF as error:
                        print(error)
                        break



            if loadChoice == 4:  # remove all loads
                df = df.iloc[0:0]    
                # df.loadPosition = 0
                # df.forceVal = 0
                print("All loads removed successfully")

            if loadChoice == 5:  # Go to main menu
                break

    if mainChoice == 3:  # Save beam and loads
        while True:
            try:
                saving_filename = input("What do you wish to name your file ?: ")
                df_for_saving = df
                # if file exists the user should rename the file
                if os.path.isfile(saving_filename + ".csv"):
                    raise FileOverwriteError('File already exists. Please enter another filename')
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
                print('Beam and load data saved as "{}" in "{}"'.format(saving_filename + ".csv", cwd))

                break
            except FileOverwriteError as error:
                print(error)

    if mainChoice == 4:  # Load beam and loads
        files = np.array(os.listdir(os.getcwd()))
        files = files[np.char.find(files, '.csv') > 0]
        nExit = np.size(files)
        files = np.hstack((files, 'Go back to main menu'))
        print('These files are available in the current working directory \n({}): '.format(os.getcwd()))
        fileChoice = displayMenu(files) - 1

        if fileChoice == nExit:
            pass

        else:
            filename = files[int(fileChoice)]

            df, beamLength, beamSupport = dataLoad(filename)

            print("Data loaded")

    if mainChoice == 5:  # Generate plot
        beamPlot(beamLength, np.array(df.loadPosition), np.array(df.forceVal), beamSupport)

        print("Beam plot created successfully")

    if mainChoice == 6:  # exits program
        print("Program closed")
        break
