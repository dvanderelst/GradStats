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

grp = data.groupby(['OFFICER_GENDER', 'SUBJECT_GENDER'])
cnt = grp.DISTRICT.count()
cnt = cnt.reset_index()

total = len(data)
gender_officers = data.OFFICER_GENDER.value_counts() / total
gender_subjects = data.SUBJECT_GENDER.value_counts() / total
p = numpy.outer(gender_officers.values, gender_subjects.values) * total

# officer_subject
m_m = p[0, 0]
f_m = p[1, 0]
o_m = p[2, 0]

m_f = p[0, 1]
f_f = p[1, 1]
o_f = p[2, 1]

m_o = p[0, 2]
f_o = p[1, 2]
o_o = p[2, 2]

norm = [f_f, f_m, f_o, m_f, m_m, m_o, o_f, o_m]

cnt['norm'] = norm

cnt['ratio'] = cnt['DISTRICT'] / cnt['norm']

table = cnt.pivot(index='OFFICER_GENDER', columns='SUBJECT_GENDER', values='ratio')
table = table.iloc[0:2, 0:2]

print(table)

#%%
from matplotlib import pyplot

for x in data.columns: print(x)

grp = data.groupby('DISTRICT')
cnt = grp.count()

cnt = cnt.reset_index()
cnt = cnt.sort_values(by='INCIDENT_NO', ascending=False)

pyplot.figure(figsize=(12,10))
pyplot.bar(range(15), cnt['INCIDENT_NO'])
pyplot.xticks(range(15), cnt['DISTRICT'], rotation=90)

pyplot.show()

##
district1 = data.query('DISTRICT == "DISTRICT 1"')
grp = data.groupby('INCIDENT_TYPE')
cnt = grp.count()
cnt = cnt.reset_index()

nr = cnt['INCIDENT_NO']
sm = nr.sum()

nr = nr/sm
#%%

explode = nr.size * [0]
explode[5] = 0.25

pyplot.figure(figsize=(6,3))
pyplot.subplot(1,2,1)
patches, texts = pyplot.pie(nr, explode=explode)
pyplot.subplot(1,2,2)
pyplot.box(False)
pyplot.axis('off')
pyplot.legend(patches, ['asssssssssssssssssssssssssss','b','c','d','e','f'], loc="right")
pyplot.show()

#%%