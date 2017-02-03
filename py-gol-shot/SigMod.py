import numpy as np
from Shot import Shot

def integrate(array, dt = 1e-6, aver_line = 4500, coeff = 1):
    aver = np.sum(array[0:aver_line])/aver_line
    return np.cumsum(array - aver) * dt * coeff


def getVacuum(shot):
    if not shot['plasma']:
        raise AttributeError('Cannot find vacuum shot for another vacuum shot (' + str(shot['shotnum']) + ')')
    # shots = []
    for i in range(shot['shotno'] - 1, shot['shotno'] - Shot.vacuumHistory, -1):
        vacuum = Shot(i)
        if not vacuum['plasma']:
            if ((vacuum['ub'] == shot['ub']) &
                    (vacuum['ucd'] == shot['ucd'])):
                return vacuum
    raise AttributeError('Cannot find vacuum shot for shot (' + str(shot['shotnum']) + ')')