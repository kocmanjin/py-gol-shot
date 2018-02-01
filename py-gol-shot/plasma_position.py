import matplotlib.pyplot as plt
from GolemShot import GolemShot
import numpy as np

def main():
    for i in xrange(25317, 25326):
        shot = GolemShot(i)
        time, dz = shot.getDz()
        plt.plot(time, dz, label=str(shot.shotNo) + (shot['wwwcomment'])[8:])
        np.savetxt(str(shot.shotNo) + 'plasma_position.txt', np.array((time, dz)).T, fmt='%f')
    return

if __name__ == '__main__':
    main()