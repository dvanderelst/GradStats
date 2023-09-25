# https://think.cs.vt.edu/corgis/python/county_demographics/county_demographics.html
import pandas
data = pandas.read_csv('counties.csv')
print(data.describe())

grp = data.groupby(['State'])
mns = grp['Age_Percent 65 and Older'].mean()