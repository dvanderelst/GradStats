#%% poverty
from matplotlib import pyplot
import pandas
data = pandas.read_csv('vaccinations.csv')

grp = data.groupby(['INCPOV1'])
t = grp.mean()
test = t.iloc[[2,0,1],:]

pyplot.plot(test.mmr)
pyplot.plot(test.hib)
pyplot.plot(test.polio)
pyplot.plot(test.hepb)

pyplot.show()