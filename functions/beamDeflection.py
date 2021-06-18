import numpy as np

def beamDeflection(positions, beamLength, loadPosition, loadForce, beamSupport):
    # Function to calculate beam deflection at "positions", with given beam length,
    # load position (and corresponding load force), and at last the support-type of
    # the beam. Returns a vector with deflections at the given positions.


    # initial constants
    E = 200*10**9 # Newton per meters squared
    I = 1*10**(-3) # Meters to the fourth power

    #input parameters and units
    x = positions # vector with elements of unit: meters
    l = beamLength # meters
    a = loadPosition # meters
    W = loadForce # newton

    less_a_pos = x[positions < a]
    geq_a_pos = x[positions >= a]

    if beamSupport == "both":
        #we sort between values <a or >=a

        y_within_l = (W * (l - a) * less_a_pos / (6 * E * I * l)) * (l ** 2 - less_a_pos ** 2 - (l - a) ** 2)
        y_outer_l = (W * a * (l - geq_a_pos) / (6 * E * I * l)) * (l ** 2 - (l - geq_a_pos) ** 2 - a ** 2)

        deflection = np.concatenate((y_within_l,y_outer_l))

    elif beamSupport == "cantilever":
        y_within_l = ((W * less_a_pos ** 2) / (6 * E * I)) * (3 * a - less_a_pos)
        y_outer_l = ((W * a ** 2) / (6 * E * I)) * (3 * geq_a_pos - a)

        deflection = np.concatenate((y_within_l, y_outer_l))

    return deflection

