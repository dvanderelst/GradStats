from matplotlib import pyplot

import pandas
data = pandas.read_csv('real_estate.csv')

pyplot.style.use('ggplot')
pyplot.scatter(data.cin/1000, data.new/1000,c=data.year)
pyplot.colorbar()
pyplot.show()