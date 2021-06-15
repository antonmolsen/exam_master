import matplotlib.pyplot as plt
import numpy as np
from functions.beamSuperposition import *


def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    positions = np.arange(0, beamLength, beamLength/2000)
    height = beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport)
    
    plt.plot(positions, height, 'r-')
    for i in range(np.size(loadPositions)):
        loadHeight = beamSuperposition(
            np.array([loadPositions[i]]), beamLength, loadPositions, loadForces, beamSupport)
        plt.arrow(loadPositions[i], loadHeight[0]*0.85, 0, loadHeight[0]*0.05, head_width=beamLength*0.02, head_length=abs(loadHeight[0]*0.05))
        plt.text(loadPositions[i]*(95/100), loadHeight[0]*0.8, r'$W_{{{}}}$'.format(i + 1))

    plt.xlim([-beamLength*(1/10), beamLength*(11/10)])
    plt.show()
