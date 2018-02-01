# import numpy as np
from SigMod import *
# from Shot import Shot
import matplotlib.pyplot as plt
from GolemShot import GolemShot


# gshot = GolemShot(23506)

# cislo = 252220
# print str(cislo)


# time, dz = shot.getDz()
# vacuum = Shot(25316)
# print vacuum['shotno']
# shot1 = Shot(23061)

# time, mc5_p = shot['mirnov_5']
# time, mc5_v = vacuum['mirnov_5']
# time, mc13_p = shot['mirnov_13']
# time, mc13_v = vacuum['mirnov_13']

# mc5_p  = integrate(mc5_p, coeff=1/(3705 * 1e-6))
# mc5_v  = integrate(mc5_v, coeff=1/(3705 * 1e-6))
# mc5 = mc5_p - mc5_v
# mc13_p = integrate(mc13_p, coeff=1/(3705 * 1e-6))
# mc13_v = integrate(mc13_v, coeff=1/(3705 * 1e-6))
# mc13 = mc13_p - mc13_v

# time = shot.getMirnovClear()[0]
# mc5_p = shot.getMirnovIntegrated()[2]
# mc5_v = shot.getVacuumShot().getMirnovIntegrated()[2]
# mc5 = shot.getMirnovClear()[2]
# mc13_p = shot.getMirnovIntegrated()[4]
# mc13_v = shot.getVacuumShot().getMirnovIntegrated()[4]
# mc13 = shot.getMirnovClear()[4]


# plt.plot(time, mc5_p, label='mc5_plasma')
# plt.plot(time, mc5_v, label='mc5_vacuum')
# plt.plot(time, mc5, label='mc5_clear')
# plt.plot(time, np.zeros(shape=len(mc5_p)))
# plt.title("mc5")
# plt.legend()
# plt.show()


# plt.plot(time, mc13_p, label='mc13_plasma')
# plt.plot(time, mc13_v, label='mc13_vacuum')
# plt.plot(time, mc13, label='mc13_clear')
# plt.plot(time, np.zeros(shape=len(mc13)))
# plt.title("mc13")
# plt.legend()
# plt.show()

# time, curr = shot['plasma_current']
# dz = 93 * (mc5 - mc13)/(mc5 + mc13)
# dz[abs(mc5) < 0.001] = float('NaN')
# dz[abs(mc13) < 0.001] = float('NaN')
# dz[abs(dz) > 100] = float('NaN')

# for shotnum in range(25090, 25092):
#     if shotnum == 25073: continue
#     if shotnum == 25078: continue
#     shot = GolemShot(shotnum)
#
#

for i in xrange(25327,25329):
    shot = GolemShot(i)
    time, dz = shot.getDz()
    img = shot['vert_camera']
    dz_c = getCenterOfMassOld(img)
    time_c = getCameraTime(img)
    # dz = dz * 3
    # print shot['wwwcomment']
    time -= shot['plasma_start']
    plt.plot(time, dz, label='mc' + str(shot.shotNo) + (shot['wwwcomment'])[8:])
    plt.plot(time_c, dz_c, label='cam' + str(shot.shotNo) + (shot['wwwcomment'])[8:])
    # np.savetxt(str(shot.shotNo) + 'plasma_position.txt', np.array((time, dz)).T, fmt='%f')
# plt.plot(time, np.zeros(shape=len(dz)), label='dz')
# print len(curr)
# print len(dz)
# plt.plot(time, curr, label='poloha')
plt.title("vertical displacement")
plt.legend()
plt.show()