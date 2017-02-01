import numpy as np
from SigMod import integrate
from Shot import Shot
import matplotlib.pyplot as plt

# link = 'http://golem.fjfi.cvut.cz/utils/data/'
# url = urllib.urlopen('http://golem.fjfi.cvut.cz/utils/data/23060/loop_voltage')
# url = urllib.urlopen(urlLink)
# myfile = url.read()
# print myfile
# f = open(os.path.join(self.shotDir, path), 'w')


shot = Shot(18874)
# vacuum = shot.getVacuum()
# shot1 = Shot(23061)
papouchST = shot.getPapouchST()

int_new = integrate(shot.papouchST[1], coeff=1/(3705 * 1e-6))

plt.plot(papouchST[0], int_new, label='mc1')


plt.show()

