import urllib
import os
import sys
import numpy as np
from SigMod import integrate


class Shot:
    link = 'http://golem.fjfi.cvut.cz/utils/data/'
    baseDir = 'shots'
    vacuumHistory = 100
    similarVacuum = 5

    def __init__(self, shotNo):
        self.shotNo = int(shotNo)
        self.shotDir = os.path.join(Shot.baseDir, str(shotNo))
        if not os.path.exists(self.shotDir):
            os.mkdir(self.shotDir)
        self.papouchST = None
        self.loopVoltage = None
        self.plasma = None
        self.ub_limit = None
        self.ucd_limit = None
        self.mc1 = None

    def getShotNo(self):
        return self.shotNo

    def getLoopVoltage(self):
        if not self.loopVoltage:
            self.loopVoltage = self.__loadDataArray__('loop_voltage')
        return self.loopVoltage

    def getPapouchST(self):
        if not self.papouchST:
            self.papouchST = self.__loadDataArray__('papouch_st')
        return self.papouchST

    def getPlasma(self):
        if not self.plasma:
            self.plasma = float(self.__loadSingleValue__('plasma')) != 0.0
        return self.plasma

    def getUbLimit(self):
        if not self.ub_limit:
            self.ub_limit = float(self.__loadSingleValue__('ub'))
        return self.ub_limit

    def getUcdLimit(self):
        if not self.ucd_limit:
            self.ucd_limit = float(self.__loadSingleValue__('ucd'))
        return self.ucd_limit

    def getVacuum(self):
        if not self.getPlasma():
            return None
        shots = []
        for i in range(self.shotNo - 1, self.shotNo - Shot.vacuumHistory, -1):
            shot = Shot(i)
            if ((shot.getUbLimit() == self.getUbLimit()) &
                (shot.getUcdLimit() == self.getUcdLimit()) &
                (not shot.getPlasma())):
                return shot
                # shots.append(shot)
                # if (len(shots) >= Shot.similarVacuum): break
        #
        # min = float('inf')
        # for shot in shots:
        #     ar = self.getMc1() - shot.getMc1()






    def getMc1(self):
        if not self.mc1:
            self.mc1 = integrate(self.getPapouchST()[1], coeff=(3705 * 1e-6))
        return self.mc1


    def __loadData__(self, path):
        if not os.path.exists(os.path.join(self.shotDir, path)):
            url = urllib.urlopen(Shot.link + str(self.shotNo) + '/' + path)
            f = open(os.path.join(self.shotDir, path), 'w')
            myfile = url.read()
            f.write(myfile)
            f.close()
        return open(os.path.join(self.shotDir, path), 'r')

    def __loadDataArray__(self, path):
        return np.loadtxt(self.__loadData__(path)).transpose()

    def __loadSingleValue__(self, path):
        return self.__loadData__(path).read()