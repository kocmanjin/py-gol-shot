import numpy as np
from pygolem_lite import Shot
# from Shot import Shot

# Maximum of shots to the past to be checked when looking for vacuum shot
Vacuum_History = 200

# integration of signal with the rid of offset
def integrate(array, dt = 1e-6, aver_line = 4500, coeff = 1):
    aver = np.sum(array[0:aver_line])/aver_line
    return np.cumsum(array - aver) * dt * coeff

# finds the vaccum shot in the past wth the same parameters. If it does not find any, raise an error
def getVacuum(shot):
    if not shot['plasma']:
        raise AttributeError('Cannot find vacuum shot for another vacuum shot (' + str(int(shot['shotno'])) + ')')
    # shots = []
    for i in range(int(shot['shotno']) - 1, int(shot['shotno']) - Vacuum_History, -1):
        vacuum = Shot(i)
        if vacuum['plasma'] < 0.5:
            if ((vacuum['ub'] == shot['ub']) &
                    (vacuum['ucd'] == shot['ucd'])):
                return vacuum
    raise AttributeError('Cannot find vacuum shot for shot (' + str(int(shot['shotno'])) + ')')


shot = Shot(23172) #shot we would like to count a vertical displacement for
vacuum = getVacuum(shot) # found vacuum shot for the elimination of non-plasma signal

# upper mirnov coil
time, mc5_p = shot['mirnov_5']
time, mc5_v = vacuum['mirnov_5']
mc5_p  = integrate(mc5_p, coeff=1/(3705 * 1e-6))
mc5_v  = integrate(mc5_v, coeff=1/(3705 * 1e-6))
mc5 = mc5_p - mc5_v # pure signal from plasma

#bottom mirnov coil
time, mc13_p = shot['mirnov_13']
time, mc13_v = vacuum['mirnov_13']
mc13_p = integrate(mc13_p, coeff=1/(3705 * 1e-6))
mc13_v = integrate(mc13_v, coeff=1/(3705 * 1e-6))
mc13 = mc13_p - mc13_v # pure signal from plasma

dz = 93 * (mc5 - mc13)/(mc5 + mc13) # calculation of displacement
# when the plasma is not alive, there should be no displacement
dz[abs(mc5) < 0.001] = float('NaN')
dz[abs(mc13) < 0.001] = float('NaN')


