#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:09:13 2019

@author: dieter
"""

# https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Questionnaire&CycleBeginYear=2015

import pandas

# https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SXQ_I.htm
sex = pandas.read_sas('SXQ_I.XPT')

#https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.htm
demo = pandas.read_sas('DEMO_I.XPT')

#https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/RHQ_I.htm
rep = pandas.read_sas('RHQ_I.XPT')


data = pandas.merge(demo, sex, on='SEQN')
data = pandas.merge(data, rep, on='SEQN')

data.to_csv('reproductive_health.csv', index=False)