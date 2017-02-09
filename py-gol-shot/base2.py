from Shot import Shot
import os
import urllib
shot = Shot(23186)

img = shot['mirnov_1']
img = shot['vert_camera']

print img.shape, img.dtype

print len(img[200][100])

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