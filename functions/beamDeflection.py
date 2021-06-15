import numpy as np
def beamDeflection(positions, beamLength, loadPosition, loadForce, beamSupport):
    # Calculation of beamDeflection


    # initial constants
    E = 200*10**9 # Newton per meters squared
    I = 1*10**(-3) # Meters to the fourth power

    #input parameters and units
    x = positions # vector with elements of unit: meters
    l = beamLength # meters
    a = loadPosition # meters
    W = loadForce # newton

    #initial list of deflection-values is empty

    deflection = []

    if beamSupport == "both":
        for i in range(np.size(positions)):
            if x[i] < a:
                y = (W * (l - a) * x[i] / (6 * E * I * l)) * (l ** 2 - x[i] ** 2 - (l - a) ** 2)
                deflection.append(y)

            elif x[i] >= a:
                y = (W * a * (l - x[i]) / (6 * E * I * l)) * (l ** 2 - (l - x[i]) ** 2 - a ** 2)
                deflection.append(y)

    elif beamSupport == "cantilever":
        for i in range(np.size(positions)):
            if x[i] < a:
                y = ((W * x[i] ** 2) / (6 * E * I)) * (3 * a - x[i])
                deflection.append(y)

            elif x[i] >= a:
                y = ((W * x[i] ** 2) / (6 * E * I)) * (3 * a - x[i])
                deflection.append(y)

    return np.array(deflection)