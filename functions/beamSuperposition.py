import numpy as np
from functions.beamDeflection import beamDeflection


def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    deflection = np.zeros(np.size(positions))

    # there are no forces applied when loadPositions or loadForces are equal to zero
    if not(np.all(loadPositions) or np.all(loadForces) == 0):
        for i in range(np.size(loadForces)):
            # loadForce i corresponds to loadPosition i
            deflection -= beamDeflection(positions, beamLength, loadPositions[i], loadForces[i], beamSupport)
    return deflection
