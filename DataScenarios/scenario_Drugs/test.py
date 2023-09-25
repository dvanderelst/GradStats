import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('drugs.csv')

grp = data.groupby(['Year'])
yr_mean = grp.mean()
yr_mean = yr_mean.reset_index()

rate12 = yr_mean["Rates_Pain Relievers Abuse Past Year_12-17"]
rate18 = yr_mean["Rates_Pain Relievers Abuse Past Year_18-25"]
rate26 = yr_mean["Rates_Pain Relievers Abuse Past Year_26+"]

yr = yr_mean["Year"]
plt.bar(yr, rate18 + rate12 + rate26)
plt.bar(yr, rate18 + rate12)
plt.bar(yr.values, rate12)






plt.show()
