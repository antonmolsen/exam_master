import numpy as np
from functions.beamDeflection import beamDeflection


def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    # Function to calculate beam deflection at "positions", with given beam length,
    # multiple load positions (and corresponding load forces), and at last the support-type of
    # the beam. Returns a vector with deflections at the given positions.
    
    # The deflection of the entire beam is assumed to be zero with no forces applied
    deflection = np.zeros(np.size(positions))


    # The deflection of the beam is calculated by adding the deflection (made negative)
    # to the starting assumtion
    for i in range(np.size(loadForces)):
            deflection -= beamDeflection(positions, beamLength, loadPositions[i], loadForces[i], beamSupport)
    return deflection
