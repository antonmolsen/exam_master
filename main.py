import numpy as np
import pandas as pd
import os

from functions.displayMenu import *
from functions.beamDeflection import beamDeflection
from functions.beamSuperposition import beamSuperposition
from functions.beamPlot import beamPlot

# Main script

# can only run one beam at a time

# Initial conditions
#empty dataframe as initial
df = pd.DataFrame({"lengthBeam":  [0],
      "supportBeam": [0],
      "loadPosition": [],
      "forcePosition": []})

while True:
    menuItems = np.array(["Configure beam", "Configure loads", "Save beam and loads", "Load beam and loads", "Generate plot", "Quit"])
    mainChoice = displayMenu(menuItems)

    if mainChoice == 1: # Configure beam
        length_current_beam = input("Please enter the length of beam in meters")
        supportItems = np.array(["both", "cantilever"])
        supportChoice = displayMenu(supportItems)
        if supportChoice == 1:
            support = "both"
        elif supportChoice == 2:
            support = "cantilever"

        df.iloc[0,0] = length_current_beam
        df.iloc[1,0] = support
        #first row of dataframe is reserved for beam information

    if mainChoice == 2: # Configure loads
        while True:
            loadItems = np.array(["See current loads", "Add a load", "Remove a load"])
            print("what do you wish to do ?")
            loadChoice = displayMenu(loadItems)

            if loadChoice == 1: # See current loads
                if sum(df.loadPosition) or sum(df.forcePosition) == 0:
                    print("There are currently no load forces on the beam")
                    pass
                else:
                    print("current loads and forces are \n")

                    # PRINT DATFRAME HERE

            if loadChoice == 2: # Add a load
                while True:
                    try:
                        load_pos = inputNumber("Enter position of load in meters: ")
                        force_val = inputNumber("Enter the force at the position: ")

                        if load_pos < 0 or load_pos > df.iloc[0,0]: # must not be longer than length of beam
                            raise

                        # load position and load force is appended to df
                        df = df.append({"loadPosition": load_pos, "forcePosition": force_val}, ignore_index=True)
                        break
                    except:
                        print("Your load position can not be lower than 0. ")
            if loadChoice == 3: # Remove a load
                #prints dataframe and the user can select which line to remove



                while True:
                    try:

                        force_val = inputNumber("Enter the force at the position: ")

                        if len(df.loadPosition) == 0:
                            raise
                        break
                    except:
                        print("There are currently no load forces on the beam")

    if mainChoice == 3: # Save beam and loads
        saving_filename = input("What do you wish to name your file ?: ")

        #file shall not overwrite old file

        s = df.to_csv(index=False)
        f = open("beam_and_support_data.csv", "w") #write
        f.write(s)
        f.close()
        #print("file saved as {} in {}".format(saving_filename, cd))



    if mainChoice == 4: # Load beam and loads
        load_filename = input("Please enter the csv file you wish to load")

        df = pd.read_csv(load_filename)

        #use dataload funktion

        print("Data loaded")

        "cantilever"
    if mainChoice == 5: # Generate plot
        beamPlot(beamLength, np.array(df.loadPosition), np.array(df.loadForce), beamSupport)
        
        # beamPlot(beamLength, ) runs here
        #ekstra plot function ?
        #print list of current forces in console

        print("Beam plot created succesfully")

    if mainChoice == 6: # exits program
        print("Program closed")
        break


