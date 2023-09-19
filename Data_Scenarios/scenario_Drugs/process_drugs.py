# https://think.cs.vt.edu/corgis/python/drugs/drugs.html
import pandas
from matplotlib import pyplot
data = pandas.read_csv('drugs.csv')
for x in data.columns: print(x)


ohio = data.query('State=="Ohio"')

pyplot.figure()
pyplot.plot(ohio.Year, ohio['Rates_Tobacco_Cigarette Past Month_12-17'])
pyplot.plot(ohio.Year, ohio['Rates_Tobacco_Cigarette Past Month_18-25'])
pyplot.plot(ohio.Year, ohio['Rates_Tobacco_Cigarette Past Month_26+'])
pyplot.legend(['Y','M','O'])


pyplot.figure()
pyplot.plot(ohio.Year, ohio['Rates_Alcohol_Dependence Past Year_12-17'])
pyplot.plot(ohio.Year, ohio['Rates_Alcohol_Dependence Past Year_18-25'])
pyplot.plot(ohio.Year, ohio['Rates_Alcohol_Dependence Past Year_26+'])
pyplot.legend(['Y','M','O'])


pyplot.show()

latest = data.query('Year == 2014')

v1 = latest["Rates_Alcohol_Need Treatment Past Year_18-25"]
v2 = latest["Rates_Alcohol_Perceptions of Risk_18-25"]

pyplot.scatter(v2,v1)
pyplot.show()

dep = "Rates_Alcohol_Need Treatment Past Year_26+"
ind = "Rates_Alcohol_Perceptions of Risk_18-25"
pyplot.show()