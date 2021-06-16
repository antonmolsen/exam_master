import numpy as np
import pandas as pd

def dataRemove(df, removed_loads):

    for i in removed_loads:
        df = df.drop(i)
        print("force {} has been removed".format(i + 1))

    # reset dataframe index
    df = df.reset_index(drop=True)
    return df