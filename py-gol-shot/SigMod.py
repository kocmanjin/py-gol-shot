import numpy as np
from Shot import Shot

def integrate(array, dt = 1e-6, aver_line = 4500, coeff = 1):
    aver = np.sum(array[0:aver_line])/aver_line
    return np.cumsum(array - aver) * dt * coeff


def getVacuum(shot):
    if shot['plasma'] < 0.5:
        raise AttributeError('Cannot find vacuum shot for another vacuum shot (' + str(int(shot['shotnum'])) + ')')
    # shots = []
    for i in range(int(shot['shotno']) - 1, int(shot['shotno']) - Shot.vacuumHistory, -1):
        vacuum = Shot(i)
        if vacuum['plasma'] < 0.5:
            if ((vacuum['ub'] == shot['ub']) &
                    (vacuum['ucd'] == shot['ucd'])):
                return vacuum
    raise AttributeError('Cannot find vacuum shot for shot (' + str(int(shot['shotnum'])) + ')')