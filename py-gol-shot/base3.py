import matplotlib.pyplot as plt
from GolemShot import GolemShot, np, movingAverage

# gshot = GolemShot(23506)

shot1 = GolemShot(26211)
shot2 = GolemShot(26212)

time, mc1_1 = shot1['mirnov_1']
time, mc1_2 = shot2['mirnov_1']


# time = np.arange(0, len(data[1]))
# uloop = data[0]
# probe1 = data[3]
# probe2 = data[4]

# plt.plot(time, uloop, label='uloop', linewidth=1)
plt.plot(time, mc1_1, label='probe1', linewidth=1)
plt.plot(time, mc1_2, label='probe2', linewidth=1)
# plt.plot(time, movingAverage(probe1, 20), label='probe1 average', linewidth=0.75)
# plt.plot(time, movingAverage(probe2, 20), label='probe2 average', linewidth=0.75)
# plt.plot(time, np.zeros(shape=len(time)), linewidth=0.5)
# plt.title("Shot " + str(shot['shotno']))
plt.legend()
plt.show()
