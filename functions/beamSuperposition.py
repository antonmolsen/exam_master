import numpy as np
from functions.beamDeflection import beamDeflection

def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):

    #there are no forces applied when loadPositions or loadForces are equal to zero
    if loadPositions or loadForces == 0:
        deflection = np.zeros(np.size(positions))
    else : # we calculate the superposition of deflections
        deflec
        for i in range(np.size(loadForces)):
            # loadForce i corresponds to loadPosition i
            deflection_row = beamDeflection(positions, beamLength, loadPositions[i], loadForces[i], beamSupport)
            np.vstack()

        deflection = deflection.sum(axis=0)

    return deflection