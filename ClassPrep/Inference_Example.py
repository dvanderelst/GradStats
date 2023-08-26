#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:33:06 2023

@author: dieter
"""


from matplotlib import pyplot
import numpy
import matplotlib


cmap = matplotlib.cm.get_cmap('Set1')

sample_size = 25
dot_size = 120
alpha=1


#make population1
c1 = [0.0] * 40
c2 = [0.25] * 40
c3 = [0.50] * 40
c4 = [0.75] * 40

population1 = numpy.array(c1 + c2 + c3 + c4)


#make population2
c1 = [0.0] * 10
c2 = [0.25] * 20
c3 = [0.50] * 40
c4 = [0.75] * 80

population2 = numpy.array(c1 + c2 + c3 + c4)


sample = numpy.random.choice(population1, size=sample_size, replace=False)
population1_colors = cmap(population1)
population2_colors = cmap(population2)
sample_colors = cmap(sample)

pyplot.figure(figsize=(15, 5))
pyplot.subplot(1,3,1)
xs = numpy.random.random(population1.size)
ys = numpy.random.random(population1.size)
pyplot.scatter(xs, ys, s=dot_size, c=population1_colors, alpha=alpha, edgecolors='k')
pyplot.xticks([])
pyplot.yticks([])
pyplot.title('Model 1: all colors equally common\n(potential world 1)')

pyplot.subplot(1,3,2)
xs = numpy.random.random(population2.size)
ys = numpy.random.random(population2.size)
pyplot.scatter(xs, ys, s=dot_size, c=population2_colors, alpha=alpha, edgecolors='k')
pyplot.xticks([])
pyplot.yticks([])
pyplot.title('Model 2: not all colors equally common \n(potential world 2)')

pyplot.subplot(1,3,3)
xs = numpy.random.random(sample.size)
ys = numpy.random.random(sample.size)
pyplot.scatter(xs, ys, s=dot_size, c=sample_colors, alpha=alpha, edgecolors='k')
pyplot.xticks([])
pyplot.yticks([])
pyplot.title('Sample')
p
pyplot.show()



