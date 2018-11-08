import numpy as np
# from pygolem_lite import Shot
from Shot import Shot

vacuumHistory = 20

def integrate(array, dt = 1e-6, aver_line = 4500, coeff = 1):
    aver = np.sum(array[0:aver_line])/aver_line
    return np.cumsum(array - aver) * dt * coeff

def movingAverage(array, dim):
    return np.convolve(array, np.ones((dim,)) / dim, mode='same')

def movingAverage2(array, dim):
    cumsum = np.cumsum(np.insert(array, 0, 0))
    return (cumsum[dim:] - cumsum[:-dim]) / float(dim)

def getCenterOfMassOld(array):
    result = np.zeros(len(array))
    for i in range(len(array)):
        mass = np.sum(array[i])
        if (mass < 156):
            result[i] = float('NaN')
            continue
        summ = 0
        for j in range(len(array[i])):
            summ += array[i][j] * j
        result[i] = summ/mass
        result[i] -= len(array[i])/2
    return result

def getCameraTime(array):
    return np.arange(0, len(array)) * 7.44e-6

def getVacuum(shot):
    if shot.shot['plasma'] < 0.5:
        raise AttributeError('Cannot find vacuum shot for another vacuum shot (' + str(int(shot.shot['shotno'])) + ')')
    # shots = []
    for i in range(int(shot.shot['shotno']) - 1, int(shot.shot['shotno']) - vacuumHistory, -1):
        vacuum = Shot(i)
        if vacuum['plasma'] < 0.5:
            if ((vacuum['ub'] == shot.shot['ub']) &
                    (vacuum['ucd'] == shot.shot['ucd'])):
                return vacuum
    raise AttributeError('Cannot find vacuum shot for shot (' + str(int(shot.shot['shotno'])) + ')')