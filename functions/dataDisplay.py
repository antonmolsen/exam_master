import pandas as pd
import numpy as np
def dataDisplay(df):
    #function that displays current forces in a dataframe in python console. Takes only dataframe as input
    # prints in console, therefore returns no value or variable

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




