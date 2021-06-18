import numpy as np
import pandas as pd


def dataLoad(filename):
    # The function loads in the data as a numpy array. The data is then
    # filtered so erroneous data is removed. funciton returns the dataframe that the program
    # usually operates with, along with the beamLength and beamSupport, loaded from file.

    df = pd.read_csv(filename)
    beamLength = df.at[0, 'beamLength']
    beamSupport = df.at[0, 'beamSupport']

    print(
        "Beam length and beam support type loaded."
    )
        
    data = [0, 0]
    read = True # Initial condition is that all data is read.
    temp_file = pd.read_csv(filename)  # Delimiter is whitespace

    arr = np.array(temp_file[['loadPosition', 'forceVal']])  # Numpy array, every row is true
    for i in range(len(arr[:, 1])):  # Length of dataset
        if not (np.isnan(arr[i, :]).any() == True):
            # Temperature boundary in 0'th collumn
            if arr[i, 0] < 0 or arr[i, 0] > beamLength:
                read = False
                print("Load {} out of range of beam length.".format(i + 1))

            if arr[i, 1] < 0:  # Growth rate in 1'st collumn
                read = False
                print("Load {} has weight under 0".format(i + 1))
    
            if read:  # We then stack i'th array on to the dataset
                data = np.vstack((data, arr[i]))
            else:
                print('Load {} removed.'.format(i + 1))
        else:
            print('No load positions or load forces detected.')
        read = True  # We reset all to true when false ones arent read


    data = np.delete(data, 0, axis=0)  # Removal of initial [0, 0] array

    if np.size(data) == 1:
        dataF = pd.DataFrame({"loadPosition": [], "forceVal": []})

    else:
        dataF = pd.DataFrame(data, columns = ['loadPosition', 'forceVal'])

    return dataF, beamLength, beamSupport
