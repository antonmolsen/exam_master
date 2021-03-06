import numpy as np
import pandas as pd

def dataRemove(df, removed_loads):
    # Function that will remove data from dataframe "df", from indexes given in numpy
    # array "removed_loads". Returns dataframe "df" with a reset index.

    for i in removed_loads:
        df = df.drop(i - 1)
        print("Force {} has been removed".format(i))

    # Reset dataframe index
    df = df.reset_index(drop=True)
    return df