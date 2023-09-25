# https://think.cs.vt.edu/corgis/python/drugs/drugs.html
import pandas
from matplotlib import pyplot
import stats
data = pandas.read_csv('drugs.csv')

for x in data.columns: print(x)

var1 = data['Totals_Pain Relievers Abuse Past Year_18-25']
var2 = data['Totals_Marijuana_Used Past Year_26+']

result = stats.simple_regression('Totals_Marijuana_Used Past Year_26+', 'Totals_Pain Relievers Abuse Past Year_18-25', data)

z = result['prediction']
pyplot.plot(var1, var2, 'g-', marker='o')
pyplot.plot(var1, z, 'red')
pyplot.show()

selected = ['Totals_Marijuana_Used Past Year_26+','Year', 'State']
states = ['Ohio','Texas']
data2 = data.loc[:,selected]
data2 = data.query('State in @states')

data.query('state == "Ohio"')