#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:34:07 2019

@author: dieter
"""
import matplotlib
from matplotlib import pyplot


fonts = []
#for f in matplotlib.font_manager.fontManager.afmist: fonts.append(f.name)
for f in matplotlib.font_manager.fontManager.ttflist: fonts.append(f.name)
fonts = list(set(fonts))

for f in fonts: print(f)

for f in fonts:
    pyplot.close('all')
    matplotlib.rcParams['font.family'] = "sans-serif"
    matplotlib.rcParams['font.sans-serif'] = f

    x = [1,2,3,4,5]
    y = [1,2,4,5,1]
    pyplot.scatter(x,y)
    pyplot.title(f)
    pyplot.show()
    pyplot.waitforbuttonpress()