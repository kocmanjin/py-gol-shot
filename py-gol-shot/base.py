from SigMod import *
from Shot import Shot
import numpy as np
import matplotlib.pyplot as plot

# obtain vacuum shot a nd plasma shot
shot = Shot(26793)  # plasma shot
shotv = Shot(26790) # vacuum shot

# obtain data from mirnov coils (already integrated)
time, mc5_p = shot['mirnov_5']
time, mc5_v = shotv['mirnov_5']
time, mc13_p = shot['mirnov_13']
time, mc13_v = shotv['mirnov_13']

# remove offset
mc5_p -= np.average(mc5_p[time < 0.004])
mc5_v -= np.average(mc5_v[time < 0.004])
mc13_p -= np.average(mc13_p[time < 0.004])
mc13_v -= np.average(mc13_v[time < 0.004])
mc5_p = movingAverage(mc5_p, 10)
mc5_v = movingAverage(mc5_v, 10)
mc13_p = movingAverage(mc13_p, 10)
mc13_v = movingAverage(mc13_v, 10)

# clear signal
mc5 = mc5_p - mc5_v
mc13 = mc13_p - mc13_v

# only for diplay original data and clear signal
# plot.plot(time, mc5_p, label='mc5_plasma')
# plot.plot(time, mc5_v, label='mc5_vac')
# plot.plot(time, mc5, label='mc5')
# plot.plot(time, mc13_p, label='mc13_plasma')
# plot.plot(time, mc13_v, label='mc13_vac')
# plot.plot(time, mc13, label='mc13')
# plot.title("mc5")
# plot.legend()
# plot.show()

# compute the plasma vertical position
dz = 93 * (mc5 - mc13)/(mc5 + mc13)
dz[abs(mc5) < 0.001] = float('NaN')
dz[abs(mc13) < 0.001] = float('NaN')
dz[abs(dz) > 100] = float('NaN')

# display the position
plot.plot(time, np.zeros(shape=len(dz)), label='dz')
plot.plot(time, dz, label='poloha')
plot.title("vertical displacement")
plot.xlim(shot['plasma_start'], shot['plasma_end'])
plot.legend()
plot.show()