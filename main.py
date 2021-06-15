import numpy as np

from functions.beamDeflection import beamDeflection
from functions.beamSuperposition import beamSuperposition

pos = np.array([1,2,3,4,5,54,45,45,45])
print("deflec", beamDeflection(pos, 20, 13, 50, "both"))

print("defelc_sup_pos =", beamSuperposition(pos, 20, 13, np.array([30,40,50,50]), "both"))
"""
Created on Mon Jun  7 22:15:28 2021

@author: antonmolsen & nicolaikongstad
"""