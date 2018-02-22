import pathlib
import DonwloadUtils
import configparser
import numpy as np

class Shot2:
    LOCAL_DIR = "C:/Users/kocman/Documents"
    GOLEM_URL = "http://golem.fjfi.cvut.cz/shots/"

    def __init__(self, shotno: int):
        self.shotno = shotno
        p = pathlib.Path(Shot2.LOCAL_DIR)
        p = p / str(shotno)
        if (not p.exists()): p.mkdir()
        cfg = p / 'das_configuration.cfg'
        if (not cfg.exists()):
            data = DonwloadUtils.download_data(Shot2.GOLEM_URL + str(shotno) + '/das_configuration.cfg')
            # print(data.read().decode())
            self.das_cfg = configparser.ConfigParser()
            self.das_cfg.read_string(data.read().decode())

    def get_das(self, das_name: str):
        if (not das_name in self.das_cfg.sections()): return None
        das = Das()
        das.status = self.das_cfg[das_name]['status'] == '1'
        das.datapath = self.das_cfg[das_name]['datapath']
        data = DonwloadUtils.download_data(Shot2.GOLEM_URL + str(self.shotno) + '/' + das.datapath)
        das.data = np.asarray(data.read().decode())
        return das


class Das():

    def __init__(self):
        self.status = None
        self.datapath = None
        self.data = None









