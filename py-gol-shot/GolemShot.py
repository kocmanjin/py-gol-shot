# from pygolem_lite import Shot
# from SigMod import *


class GolemShot:

    shots_dir = "c:\\Users\\kocman\\Documents"

    def __init__(self, shotNo: int):
        # Shot.__init__(self, shotNo)
        # self.shot = Shot(shotNo)
        # Shot.__init__(self, str(shotNo))
        self.mirnovIntegrated = None
        self.mirnovClear = None
        self.vacuum = None
        self.dz = None

    def getVacuumShot(self):
        if self.vacuum is None:
            # self.vacuum = GolemShot(getVacuum(self)['shotno'])
            self.vacuum = GolemShot(25316)
        return self.vacuum


    def getMirnovIntegrated(self):
        if self.mirnovIntegrated is None:
            self.mirnovIntegrated = []
            time, mc1 = self['mirnov_1']
            time, mc5 = self['mirnov_5']
            time, mc9 = self['mirnov_9']
            time, mc13 = self['mirnov_13']
            self.mirnovIntegrated.append(time)
            self.mirnovIntegrated.append(integrate(mc1, coeff=1/(3705 * 1e-6)))
            self.mirnovIntegrated.append(integrate(mc5, coeff=1/(3705 * 1e-6)))
            self.mirnovIntegrated.append(integrate(mc9, coeff=1/(3705 * 1e-6)))
            self.mirnovIntegrated.append(integrate(mc13, coeff=1/(3705 * 1e-6)))
        return self.mirnovIntegrated

    def getMirnovClear(self):
        if self.mirnovClear is None:
            self.mirnovClear = [None] * 5
            vacuum = self.getVacuumShot();
            integrated_p = self.getMirnovIntegrated()
            integrated_v = vacuum.getMirnovIntegrated()
            self.mirnovClear[0] = integrated_v[0];
            self.mirnovClear[1] = integrated_p[1] - integrated_v[1]
            self.mirnovClear[2] = integrated_p[2] - integrated_v[2]
            self.mirnovClear[3] = integrated_p[3] - integrated_v[3]
            self.mirnovClear[4] = integrated_p[4] - integrated_v[4]
        return self.mirnovClear

    def getDz(self):
        if self.dz is None:
            self.dz = 93 * (self.getMirnovClear()[2] - self.getMirnovClear()[4]) / (self.getMirnovClear()[2] + self.getMirnovClear()[4])
            self.dz[abs(self.getMirnovClear()[2]) < 0.001] = float('NaN')
            self.dz[abs(self.getMirnovClear()[4]) < 0.001] = float('NaN')
            self.dz[abs(self.dz) > 100] = float('NaN')
        return self.getMirnovClear()[0], self.dz
