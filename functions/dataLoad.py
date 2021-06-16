import numpy as np
import pandas as pd


def dataLoad(filename):
    # The function loads in the data as a numpy array. The data is then
    # filtered so known bad data is removed.

    # initial condition is that the data is accepted

    df = pd.read_csv(filename)
    
    beamLength = df.at[0, 'beamLength']
    beamSupport = df.at[0, 'beamSupport']
        
    data = [0, 0]
    read = True
    temp_file = pd.read_csv(filename)  # delimiter is whitespace

    arr = np.array(temp_file[['loadPosition', 'forceVal']])  # numpy array, every row is true

    for i in range(len(arr[:, 1])):  # length of dataset
        if not(np.isnan(arr[i, :]).any == True):
            # temperature boundary in 0'th collumn
            if arr[i, 0] < 0 or arr[i, 0] > beamLength:
                read = False
                print("Load {} out of range of beam length.".format(i + 1))
    
            if arr[i, 1] < 0:  # growth rate in 1'st collumn
                read = False
                print("Load {} has weight under 0".format(i + 1))
    
            if read:  # we then stack i'th array on to the dataset
                data = np.vstack((data, arr[i]))
            else:
                print('Load {} removed.'.format(i + 1))
            
        else:
            print('Either load position or load force missing. Data removed.')

        read = True  # we reset all to true when false ones arent read


    data = np.delete(data, 0, axis=0)  # removal of initial [0, 0] array
    dataF = pd.DataFrame(data, columns = ['loadPosition', 'forceVal']) # original data. Is never changed in script

    return dataF, beamLength, beamSupport
