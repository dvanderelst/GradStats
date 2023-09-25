#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:02:04 2019

@author: dieter

NAR: Narcan Administered, No Transport. Narcan was administered for a heroin
overdose; no transport to the hospital was made.
NART: Narcan Administered With Transport. Narcan was administered for a
heroin overdose; the patient was transported to the hospital by a medic
transport.
"""

import pandas
from matplotlib import pyplot

data = pandas.read_csv('raw_emergencies.csv')
types = data.DISPOSITION_TEXT.value_counts()

# %% Get overdoses
NART = data.DISPOSITION_TEXT.str.startswith("NART")
NAR = data.DISPOSITION_TEXT.str.startswith("NAR")
selected = (NART + NAR) > 0

overdoses = data.loc[selected]
times = pandas.to_datetime(overdoses.CREATE_TIME_INCIDENT)
days = times.dt.day_name()
hours = times.dt.hour
months = times.dt.month

overdoses['DAY'] = days
overdoses['HOUR'] = hours
overdoses['MONTH'] = months
overdoses.to_csv('overdoses.csv', sep=',', index=False)

