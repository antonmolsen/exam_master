import matplotlib.pyplot as plt
from functions.beamDeflection import beamSuperposition


def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    positions = np.arange(0, beamLength, 200)
    height = beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport)

    plt.plot(position, height, or --)
    for i in range(np.size(loadPositions)):
        loadHeight = beamSuperposition(
            np.array([loadPositions[i]]), beamLength, loadPositions, loadForces, beamSupport)
        plt.arrow(loadPositions[i], loadHeight[0]*(15/10), 0, loadHeight[0]**(11/10))
        plt.text(loadPositions[i], loadHeight[0]*2, r'$W_{{}}$'.format(i + 1))

    plt.xlim([-1, beamLength + 1])
    plt.show()
