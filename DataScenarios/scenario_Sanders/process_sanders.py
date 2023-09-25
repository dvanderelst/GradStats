import pandas
import seaborn
from matplotlib import pyplot
import numpy

data = pandas.read_csv('sanders.csv')
data['log'] = numpy.log2(data['expenditure'])

last = data.query('year==2015 and sex=="BTSX"')
last_usa = data.query('year==2015 and sex=="BTSX" and code=="USA"')


pyplot.figure()
seaborn.scatterplot(x='log', y='atbirth', hue='region', data=last)
pyplot.scatter(last_usa['log'], last_usa['atbirth'], s=100,c='black')

pyplot.show()


#%%
last['more'] = last['atbirth'] > float(last_usa.atbirth)
higher = last.query('more')


pyplot.figure()
seaborn.scatterplot(x='log', y='atbirth', hue='region', data=higher)
pyplot.scatter(last_usa['log'], last_usa['atbirth'], s=100,c='black')
pyplot.vlines(last_usa.log-1, 75, 84, linestyles='-.')

pyplot.show()
