import imageio.v3 as iio
import os
filenames=['n1.png','n2.png']
l=[]
for i in filenames:
    l.append(iio.imread(i))
iio.imwrite('ige.gif',l,duration=500,loop=0)
os.startfile('ige.gif')