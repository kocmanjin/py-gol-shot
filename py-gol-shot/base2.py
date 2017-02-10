from Shot import Shot
from SigMod import *
import numpy as np
import sys
import urllib
import matplotlib.pyplot as plt


shot = Shot(23186)

# img = shot['mirnov_1']
img = shot['vert_camera']

print img.shape

dz_old = getCenterOfMassOld(img)
time = np.arange(0, len(dz_old))
plt.plot(time, dz_old, label='dz')
plt.show()


# print img.shape, img.dtype

# f = open("test.txt", "w")

# for i in range(len(img)):
#     for j in range(len(img[i])):
#         f.write(str(i) + " " + str(j) + " " + str(img[i][j]) + "\n")
#     f.write("\n")

# print img.shape()
# base_url = Shot.link_img
# url = 'diagnostics/Radiation/0211FastCamera.ON/1/CorrectedRGB.png'
# dest = base_url + str(23186) + '/' + url
# print dest
# url_link = urllib.urlopen(dest)
# f = open('test.png', 'wb')
# myfile = url_link.read()
# f.write(myfile)
# f.close()