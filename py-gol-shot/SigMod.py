import numpy as np


def integrate(array, dt = 1e-6, aver_line = 4500, coeff = 1):
    aver = np.sum(array[0:aver_line])/aver_line
    return np.cumsum(array - aver) * dt * coeff
