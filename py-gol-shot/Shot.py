import urllib.request
import os
import numpy as np
from PIL import Image

# HTTP_DATA_LINK = 'http://golem.fjfi.cvut.cz/utils/data/'
# SAVE_DIR = 'shots'

class Shot:
    link = 'http://golem.fjfi.cvut.cz/utils/data/'
    link_homepage = 'http://golem.fjfi.cvut.cz/shots/'
    baseDir = 'shots'
    vacuumHistory = 200
    similarVacuum = 5

    def __init__(self, shotNo):
        self.shotNo = int(shotNo)
        if (Shot.baseDir is not None):
            self.shotDir = os.path.join(Shot.baseDir, str(shotNo))
            # if not os.path.exists(SAVE_DIR):
            #     os.mkdir(SAVE_DIR)
            if not os.path.exists(self.shotDir):
                os.mkdir(self.shotDir)
        self.papouchST = None
        self.papouchKO = None
        self.plasma_current = None
        self.loopVoltage = None
        self.plasma = None
        self.ub_limit = None
        self.ucd_limit = None
        self.wwwcomment = None
        self.plasma_start = None
        self.plasma_end = None
        self.img = None
        self.rigolC = None


    def __getitem__(self, item):
        if item == 'mirnov_1':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[1]
        elif item == 'mirnov_5':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[2]
        elif item == 'mirnov_9':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[3]
        elif item == 'mirnov_13':
            return self.__getPapouchST__()[0], self.__getPapouchST__()[4]
        elif item == 'papouchKo':
            return self.__getPapouchKO__()
        elif item == 'plasma_current':
            return self.__getPlasmaCurrent__()[0], self.__getPlasmaCurrent__()[1]
        elif item == 'rigolC':
            return self.__getRigolC__()
        elif item == 'plasma':
            return float(self.__getPlasma__())
        elif item == 'shotno':
            return float(self.__getShotNo__())
        elif item == 'ub':
            return float(self.__getUbLimit__())
        elif item == 'ucd':
            return float(self.__getUcdLimit__())
        elif item == 'plasma_start':
            return float(self.__getPlasmaStart__())
        elif item == 'plasma_end':
            return float(self.__getPlasmaEnd__())
        elif item == 'wwwcomment':
            return self.__getWwwComment__()
        elif item == 'vert_camera':
            return self.__getVertCamera__()
        raise AttributeError("Unknown diagnostics '" + item + "'")


    def __getShotNo__(self):
        return self.shotNo

    def __getLoopVoltage__(self):
        if not self.loopVoltage:
            self.loopVoltage = self.__loadDataArray__('loop_voltage')
        return self.loopVoltage

    def __getPapouchST__(self):
        if self.papouchST is None:
            self.papouchST = self.__loadDataArray__('papouch_st')
        return self.papouchST

    def __getPapouchKO__(self):
        if self.papouchKO == None:
            self.papouchKO = self.__loadDataArray__('papouch_ko')
        return self.papouchKO

    def __getRigolC__(self):
        if self.rigolC == None:
            self.rigolC = self.__loadDataArrayHomepage__('rigolC', 'DAS/0417RigolDS1074c.ON/data_all')
        return self.rigolC

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

    def __getWwwComment__(self):
        if not self.wwwcomment:
            self.wwwcomment = self.__loadSingleValue__('wwwcomment')
        return self.wwwcomment

    def __getPlasmaStart__(self):
        if not self.plasma_start:
            self.plasma_start = float(self.__loadSingleValue__('plasma_start'))
        return self.plasma_start

    def __getPlasmaEnd__(self):
        if not self.plasma_end:
            self.plasma_end = float(self.__loadSingleValue__('plasma_end'))
        return self.plasma_end

    def __getVertCamera__(self):
        if not self.img:
            self.img = self.__loadImage__('vert_camera.png', 'diagnostics/Radiation/0211FastCamera.ON/1/CorrectedRGB.png')
        return self.img

    # def getMc1(self):
    #     if not self.mc1:
    #         self.mc1 = integrate(self.getPapouchST()[1], coeff=(3705 * 1e-6))
    #     return self.mc1


    def __loadData__(self, path, url=None, base_url=None, binary=False):
        if not base_url:
            base_url = Shot.link
        if not url:
            url = path
        if not os.path.exists(os.path.join(self.shotDir, path)):
            link = base_url + str(self.shotNo) + '/' + url
            print(link)
            url_link = urllib.request.urlopen(base_url + str(self.shotNo) + '/' + url)
            # url_link = urllib.urlopen(base_url + str(self.shotNo) + '/' + url)
            f = open(os.path.join(self.shotDir, path), 'w' + ('b' if binary else ''))
            myfile = url_link.read().decode()
            f.write(myfile)
            f.close()
        return open(os.path.join(self.shotDir, path), 'r' + ('b' if binary else ''))

    def __loadImage__(self, path, url=None):
        img = Image.open(self.__loadData__(path, url, Shot.link_homepage, 'wb')).convert('L')
        img = np.flip(img, 0).transpose()
        return np.array(img)

    def __loadDataArrayHomepage__(self, path, url):
        dat = self.__loadData__(path, url, Shot.link_homepage)
        return np.loadtxt(dat).transpose()

    def __loadDataArray__(self, path, url=None):
        return np.loadtxt(self.__loadData__(path, url)).transpose()

    def __loadSingleValue__(self, path, url=None):
        return self.__loadData__(path, url).read()

