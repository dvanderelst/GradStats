import pandas
from matplotlib import pyplot
import seaborn

data = pandas.read_csv('smoking.csv')
data= data.sort_values(by=['State', 'Year'])

seaborn.lineplot(x='Year', y='Smoke everyday', data=data)

pyplot.show()

