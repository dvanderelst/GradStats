import pandas
from matplotlib import pyplot

pyplot.style.use('ggplot')

data = pandas.read_csv('climate.csv')

HIC = data.query('iso=="HIC"')
LIC = data.query('iso=="LIC"')
USA = data.query('iso=="USA"')
NOR = data.query('iso=="NOR"')

pyplot.subplot(1,2,1)
pyplot.plot(HIC.year, HIC.co2)
pyplot.plot(LIC.year, LIC.co2)
pyplot.plot(USA.year, USA.co2)

pyplot.subplot(1,2,2)
pyplot.plot(HIC.year, HIC.renewable)
pyplot.plot(LIC.year, LIC.renewable)
pyplot.plot(USA.year, USA.renewable, linewidth=5, alpha=0.5)
pyplot.plot(NOR.year, NOR.renewable)
pyplot.ylim([0, 100])
pyplot.legend(['HIC','LIC', 'USA'])

pyplot.show()
