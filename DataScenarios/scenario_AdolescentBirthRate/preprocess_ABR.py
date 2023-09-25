import pandas
import seaborn
import numpy
from matplotlib import pyplot

# Birth rates
selected = [1, 2, 3, 6]
rates = pandas.read_excel('raw_data.xls', sheet_name='Sheet3')
rates = rates.iloc[:, selected]
rates.columns = ['year', 'region', 'country', 'rate']

# Demographics
demographics = pandas.read_excel('raw_data.xls', sheet_name='Sheet8')

i = 0
for x in demographics.columns:
    print(i, x)
    i = i + 1

selected = [1, 18]
demographics = demographics.iloc[:, selected]
demographics.columns = ['country' , 'income']

# Mortality
mortality = pandas.read_excel('mortality.xls', sheet_name='data')

# Merge
data = pandas.merge(rates, demographics, on=['country'])
data = pandas.merge(data, mortality,  on=['country', 'year'])

# Remap
data['income_levels'] = data['income']
map = {'Low income': 0,
       'Lower middle income': 1,
       'Upper middle income': 2,
       'High income': 3}
data = data.replace({"income_levels": map})


data.to_csv('birth.csv', index=0)

#
# Plot
#

data['rate'] = numpy.log10(data['rate'])
data['under_five'] = numpy.log10(data['under_five'])

seaborn.barplot(x='income_levels', y='rate', data=data)
pyplot.show()

seaborn.scatterplot(x='under_five', y='rate', data=data)
pyplot.show()

