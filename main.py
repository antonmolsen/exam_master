import numpy as np
import pandas as pd

from functions.displayMenu import *
from functions.beamDeflection import beamDeflection
from functions.beamSuperposition import beamSuperposition
from functions.beamPlot import beamPlot

# Main script

# Initial conditions
loadForces = []
loadPositions = []
positions = []

#empty dataframe as inital
df = {"lengthBeam":  [1,2,3],
      "supportBeam": [1,2,3],
      "loadPosition": [1,2,3],
      "forcePosition": [1,2,3]}
df = pd.DataFrame(df, columns = ["lengthBeam", "supportBeam", "loadPosition", "forcePosition"])

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

        # data is appended to length and support list



    if mainChoice == 2: # Configure loads
        while True:
            loadItems = np.array(["See current loads", "Add a load", "Remove a load"])
            print("what do you wish to do ?")
            loadChoice = displayMenu(loadItems)

            if loadChoice == 1: # See current loads
                if np.sum(loadForces) == 0:
                    print("there are currently no load forces on the beam")
                    pass

                else:
                    print("current loads are \n")
                    for i in range(np.size(loadForces))
                        print("force at {} meters with {} newton".format(loadPositions[i], loadForces[i]))

            if loadChoice == 2: # Add a load
                while True:
                    try:
                        load_pos = inputNumber("Enter position of load in meters: ")
                        force_val = inputNumber("Enter the force at the position: ")

                        if load_pos < 0:
                            raise
                        break
                    except:
                        print("your load position can not be lower than 0. ")
            if loadChoice == 3: # Remove a load


    if mainChoice == 3: # Save beam and loads
        "cantilever"
    if mainChoice == 4: # Load beam and loads

        "cantilever"
    if mainChoice == 5: # Generate plot
        # beamPlot(beamLength, ) runs here

        print("Beam plot created succesfully")

    if mainChoice == 6: # exits program
        print("Program closed")
        break


