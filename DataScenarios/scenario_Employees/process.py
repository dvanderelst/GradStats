#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:55:17 2019

@author: dieter
"""

import pandas
from matplotlib import pyplot

data= pandas.read_csv('pay.csv', thousands=',')
data.RACE.value_counts()
white = data.query('RACE=="WHITE"')
black = data.query('RACE=="BLACK"')

pyplot.hist(white.ANNUAL_RT,alpha=0.5,bins=50)
pyplot.hist(black.ANNUAL_RT,alpha=0.5,bins=50)

high_pay = data.query('ANNUAL_RT > 100000')
cnts = high_pay.RACE.value_counts()

pyplot.figure()
pyplot.bar(range(6), cnts)
pyplot.show()



