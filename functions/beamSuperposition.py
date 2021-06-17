import numpy as np
from functions.beamDeflection import beamDeflection


def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    deflection = np.zeros(np.size(positions))
    # Function to calculate deflection at given positions, with multiple
    # load positions (and corresponding load forces). As in "beamDeflection",
    # "beamSupport" is also needed as input



    # there are no forces applied when loadPositions or loadForces are equal to zero
    for i in range(np.size(loadForces)):
            # loadForce i corresponds to loadPosition i
            deflection -= beamDeflection(positions, beamLength, loadPositions[i], loadForces[i], beamSupport)
    return deflection
