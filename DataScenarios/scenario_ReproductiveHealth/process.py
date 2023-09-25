#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:11:17 2019

@author: dieter
"""

import pandas
import seaborn
from matplotlib import pyplot

data = pandas.read_csv('reproductive_health.csv')
women = data.query('RIAGENDR==2 and RHD180 < 35 and SXD031 < 35')

count = women.RHD180.value_counts()
pyplot.bar(count.index, count)
pyplot.show()

count = women.SXD031.value_counts()
pyplot.bar(count.index, count)
pyplot.show()

grp = women.groupby(['SXD031'])
mns = grp.mean()
mns = mns.reset_index()

pyplot.figure()
pyplot.scatter(mns.SXD031, mns.RHD180)

pyplot.figure()
pyplot.scatter(mns.SXD031, mns.RHD180-mns.SXD031)

pyplot.figure()
seaborn.lineplot(x='SXD031', y='RHD180', data=women)
