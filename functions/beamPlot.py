import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from functions.beamSuperposition import *


def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    # Function to create plot of current beam with current loads.
    # To prevent the plot from being too filled with loaddata, information 
    # about each load are displayed as "w1", "w2", etc. in the console.

    positions = np.arange(0, beamLength, beamLength/2000)
    height = beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport)
    minHeight = min(height)
    maxHeight = max(height)
    dHeigth = maxHeight - minHeight
    
    temp = {'':[],'Forces [N]':[], 'Positions [m]':[]}
    weights = pd.DataFrame(data = temp)
    
    plt.plot(positions, height, 'r-')
    for i in range(np.size(loadPositions)):
        loadHeight = beamSuperposition(
            np.array([loadPositions[i]]), beamLength, loadPositions, loadForces, beamSupport)
        plt.arrow(loadPositions[i], loadHeight[0] - minHeight*0.1, 0, minHeight*0.05, head_width=beamLength*0.02, head_length=abs(minHeight*0.03))
        plt.text(loadPositions[i] - beamLength*(0.02), loadHeight[0] - minHeight*0.15, r'$W_{{{}}}$'.format(i + 1))
        
        weights = weights.append({'':'W{}'.format(i + 1),'Forces [N]':loadForces[i], 'Positions [m]':loadPositions[i]}, ignore_index=True)

    
    plt.title('Beam deflection with support type: {:s}'.format(beamSupport))
    plt.xlim([-beamLength*(1/10), beamLength*(11/10)])
    plt.ylim([minHeight - dHeigth*0.25, maxHeight + dHeigth*0.25])
    plt.xlabel('Length [m]')
    plt.ylabel('Deflection [m]')
    plt.show()
    print(weights.to_string(index = False))
    
    
