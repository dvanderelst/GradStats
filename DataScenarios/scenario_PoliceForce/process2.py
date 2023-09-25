#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:06:34 2019

@author: dieter
"""




import numpy
import pandas

data = pandas.read_csv('PoliceForce.csv', parse_dates=['INCIDENT_DATE'])

dates = data['INCIDENT_DATE']
year = dates.dt.year
data['year'] = year

grp = data.groupby(['INCIDENT_DESCRIPTION', 'year', 'SUBJECT_RACE'])
cnt = grp.count()
cnt = cnt.reset_index()

subset = cnt.query('INCIDENT_DESCRIPTION=="INJURY TO PRISONER"')

#%%
import seaborn
month = dates.dt.month
data['MONTH'] = month
grp = data.groupby(['INCIDENT_DESCRIPTION','MONTH'])
cnt = grp.count()
cnt = cnt.reset_index()

seaborn.lineplot(x='MONTH',y='INCIDENT_NO', hue='INCIDENT_DESCRIPTION',data=cnt)

pyplot.xticks(range(1,4), ['J','F','M'])
pyplot.show()