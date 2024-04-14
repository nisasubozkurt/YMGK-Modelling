#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
from matplotlib.pyplot import *
import os


def poliplot(fnom):
    data = loadtxt(fnom)
##    data[where(data == 0)] = nan
    xlabel('b');  ylabel(r'$\lambda$');  title('Henon map')
##    print data
    data2 = zeros((data.shape[0], data.shape[1], 3), dtype='uint8')
##    print where(data == 1)
    # Make colors:
    blue = array([0, 0, 255], dtype='uint8')
    green = array([0, 255, 0], dtype='uint8')
    red = array([255, 0, 0], dtype='uint8')
    cyan = array([0, 255, 255], dtype='uint8')
    magenta = array([255, 0, 255], dtype='uint8')
    yellow = array([255, 255, 0], dtype='uint8')
    orange = array([255, 127, 0], dtype='uint8')
    white = array([255, 255, 255], dtype='uint8')
    darkgreen =  array([0, 127, 0], dtype='uint8')
    colori = {0: white, 1: blue, 2: green, 4: yellow, 8: magenta,
              3: cyan, 32: red, 5: orange, 7: darkgreen}
    # Get colors:
    for j1 in range(data.shape[0]):
        for j2 in range(data.shape[1]):
            if data[j1, j2] in colori:
                data2[j1, j2, :] = colori[data[j1, j2]]
##    data2[where(data == 0), :] = white[:]
##    data2[where(data == 1), :] = blue[:]
##    data2[where(data == 2), :] = green[:]
##    data2[where(data == 4), :] = yellow[:]
##    data2[where(data == 8), :] = magenta[:]
##    data2[where(data == 3), :] = cyan[:]
##    data2[where(data == 33), :] = red[:]
    # Рисуем график:
    imshow(data2, interpolation='nearest', origin='lower',
           extent=(-0.5, 0.5, 0.0, 2.0), aspect=0.5)
    picnom = os.path.splitext(fnom)[0] + '.png'
    savefig(picnom)
    show()


if __name__ == '__main__':
    poliplot('henon.txt') # put here your data file
##    poliplot('Fortran_Henon/fortran_Henon.txt')
##    poliplot('D_Henon/d_Henon.txt')
##    poliplot('Go_Henon/go_Henon.txt')




