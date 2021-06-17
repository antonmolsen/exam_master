import numpy as np
import pandas as pd

def dataRemove(df, removed_loads):
    #


    for i in removed_loads:
        df = df.drop(i - 1)
        print("force {} has been removed".format(i))

    # reset dataframe index
    df = df.reset_index(drop=True)
    return df