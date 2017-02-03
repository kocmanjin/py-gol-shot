import urllib
import os
import sys
import numpy as np

class Shot:
    link = 'http://golem.fjfi.cvut.cz/utils/data/'
    baseDir = 'shots'
    vacuumHistory = 200
    similarVacuum = 5

    def __init__(self, shotNo):
        self.shotNo = int(shotNo)
        self.shotDir = os.path.join(Shot.baseDir, str(shotNo))
        if not os.path.exists(self.shotDir):
            os.mkdir(self.shotDir)
        self.papouchST = None
        self.plasma_current = None
        self.loopVoltage = None
        self.plasma = None
        self.ub_limit = None
        self.ucd_limit = None
        self.mc1 = None


    def __getitem__(self, item):
        if item == 'mirnov_1':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[1]
        elif item == 'mirnov_5':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[2]
        elif item == 'mirnov_9':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[3]
        elif item == 'mirnov_13':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[4]
        elif item == 'plasma_current':
            return self.__getPlasmaCurrent__()[0], self.__getPlasmaCurrent__()[1]
        elif item == 'plasma':
            return float(self.__getPlasma__())
        elif item == 'shotno':
            return float(self.__getShotNo__())
        elif item == 'ub':
            return float(self.__getUbLimit__())
        elif item == 'ucd':
            return float(self.__getUcdLimit__())
        raise AttributeError("Unknown diagnostics '" + item + "'")



    def __getShotNo__(self):
        return self.shotNo

    def __getLoopVoltage__(self):
        if not self.loopVoltage:
            self.loopVoltage = self.__loadDataArray__('loop_voltage')
        return self.loopVoltage

    def __getPapouchST__(self):
        if self.papouchST == None:
            self.papouchST = self.__loadDataArray__('papouch_st')
        return self.papouchST

    def __getPlasmaCurrent__(self):
        if self.plasma_current == None:
            self.plasma_current = self.__loadDataArray__('plasma_current')
        return self.plasma_current

    def __getPlasma__(self):
        if not self.plasma:
            self.plasma = float(self.__loadSingleValue__('plasma'))
        return self.plasma

    def __getUbLimit__(self):
        if not self.ub_limit:
            self.ub_limit = float(self.__loadSingleValue__('ub'))
        return self.ub_limit

    def __getUcdLimit__(self):
        if not self.ucd_limit:
            self.ucd_limit = float(self.__loadSingleValue__('ucd'))
        return self.ucd_limit


    # def getMc1(self):
    #     if not self.mc1:
    #         self.mc1 = integrate(self.getPapouchST()[1], coeff=(3705 * 1e-6))
    #     return self.mc1


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