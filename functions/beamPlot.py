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


    
    if dHeigth == 0: # Is nessesary to be able to plot without loads
        minHeight = -1
        maxHeight = 1
    
    temp = {'':[],'Forces [N]':[], 'Positions [m]':[]} # Makes a dataframe to display loads.
    weights = pd.DataFrame(data = temp)
    
    plt.plot(positions, height, 'r-', label = "{:.1f} m beam".format(beamLength))
    
    for i in range(np.size(loadPositions)):
        # Plots text and arrows to show the load position. They all scale with the size of the plot.
        
        loadHeight = beamSuperposition(
            np.array([loadPositions[i]]), beamLength, loadPositions, loadForces, beamSupport)
        
        plt.arrow(loadPositions[i], loadHeight[0] - minHeight*0.1, 0, minHeight*0.05, width = beamLength*0.005, head_width=beamLength*0.02, head_length=abs(minHeight*0.03))
        plt.text(loadPositions[i] - beamLength*(0.02), loadHeight[0] - minHeight*0.15, r'$W_{{{}}}$'.format(i + 1))
        
        weights = weights.append({'':'W{}'.format(i + 1),'Forces [N]':loadForces[i], 'Positions [m]':loadPositions[i]}, ignore_index=True)

    
    if beamSupport == 'both':
        plt.plot([positions[0], positions[-1]],[height[0], height[-1]], 'ok', label = 'Anchorpoints')
        
    elif beamSupport == 'cantilever':
        plt.plot(positions[0],height[0], 'ok', label = 'Anchorpoint')
        


    plt.title('Beam deflection with support type: {:s}'.format(beamSupport))
    plt.xlim([-beamLength*(1/10), beamLength*(11/10)])
    plt.ylim([minHeight - dHeigth*0.25, maxHeight + dHeigth*0.5])
    plt.xlabel('Length [m]')
    plt.ylabel('Deflection [m]')
    plt.plot([], [], ' ', label = "Maximum deflection is {:.2E}".format(dHeigth))
    plt.legend()
    plt.tight_layout()
    plt.show()

    if len(loadPositions) == 0:
        print("\nThere are currently no load forces on the beam.")

    else:
        print(weights.to_string(index = False)) # Shows the details of the current loads.
    
    
