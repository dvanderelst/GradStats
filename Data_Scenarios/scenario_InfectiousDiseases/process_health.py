# https://think.cs.vt.edu/corgis/python/drugs/drugs.html
import pandas
from course import stats
from matplotlib import pyplot
data = pandas.read_csv('health.csv')
for x in data.columns: print(x)

pyplot.style.use('ggplot')

#
# MEASLES Vaccination
#


developed = 1963
selected = data.query('disease=="MEASLES"')
grp = selected.groupby(['year'])
sm = grp.sum()
sm = sm.reset_index()

pyplot.plot(sm.year, sm.number/1000)
pyplot.vlines(developed, 0, 800)
pyplot.show()


#
# MMR Vaccination
#

developed = [1963, 1967, 1969]
diseases = ['MEASLES', 'MUMPS', 'RUBELLA']

selected = data.query('disease in @diseases')
grp = selected.groupby(['year'])
sm = grp.sum()
sm = sm.reset_index()

pyplot.plot(sm.year, sm.number/1000)
pyplot.vlines(developed[0], 0, 800)
pyplot.vlines(developed[1], 0, 800)
pyplot.vlines(developed[2], 0, 800)
pyplot.legend(['Cases', 'Vac. measles', 'Vac. mumps', 'Vac. Rubella'])
pyplot.xlabel('Year')
pyplot.ylabel('Cases (x 1000)')
pyplot.show()