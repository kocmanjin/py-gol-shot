import numpy as np
from SigMod import *
from Shot import Shot
import matplotlib.pyplot as plt

# link = 'http://golem.fjfi.cvut.cz/utils/data/'
# url = urllib.urlopen('http://golem.fjfi.cvut.cz/utils/data/23060/loop_voltage')
# url = urllib.urlopen(urlLink)
# myfile = url.read()
# print myfile
# f = open(os.path.join(self.shotDir, path), 'w')

shot = Shot(23172)
vacuum = getVacuum(shot)
# shot1 = Shot(23061)
time, mc5_p = shot['mirnov_5']
time, mc5_v = vacuum['mirnov_5']
time, mc13_p = shot['mirnov_13']
time, mc13_v = vacuum['mirnov_13']

mc5_p  = integrate(mc5_p, coeff=1/(3705 * 1e-6))
mc5_v  = integrate(mc5_v, coeff=1/(3705 * 1e-6))
mc5 = mc5_p - mc5_v
mc13_p = integrate(mc13_p, coeff=1/(3705 * 1e-6))
mc13_v = integrate(mc13_v, coeff=1/(3705 * 1e-6))
mc13 = mc13_p - mc13_v

# plt.plot(time, mc5_p, label='mc5')
# plt.plot(time, mc5_v, label='mc5')
# plt.plot(time, mc5, label='mc5')

# plt.plot(time, mc13_p, label='mc5')
# plt.plot(time, mc13_v, label='mc5')
# plt.plot(time, mc13, label='mc5')
# plt.plot(time, np.zeros(shape=len(mc5)), label='mc5')

# plt.show()

# time, curr = shot['plasma_current']
dz = 93 * (mc5 - mc13)/(mc5 + mc13)
dz[abs(mc5) < 0.001] = float('NaN')
dz[abs(mc13) < 0.001] = float('NaN')

plt.plot(time, dz, label='poloha')
# print len(curr)
# print len(dz)
# plt.plot(time, curr, label='poloha')

plt.show()



