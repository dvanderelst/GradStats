import pandas
import seaborn
from matplotlib import pyplot
# pip install savreaderwriter
import savReaderWriter as spss
import numpy

filename = 'data.sav'

raw_data = spss.SavReader(filename, returnHeader=True, ioUtf8=True)
raw_data_list = list(raw_data)
df = pandas.DataFrame(raw_data_list)

header = df.iloc[0, :]
data = df.iloc[1:, :]
data.columns = header

country = data['country']

map = {1: 'Denmark',
       2: 'France',
       3: 'Germany',
       4: 'Italy',
       5: 'Netherlands',
       6: 'Spain',
       7: 'Sweden',
       8: 'United Kingdom'}

country = country.map(map)
data['country'] = country

# replace all the missing values

data = data.replace(98, numpy.NAN)
data = data.replace(99, numpy.NAN)

data.to_csv('media.csv', index=False)
# %% Check to see whether the countries have been assigned correctly.

# compare these numbers with the numbers in table 1 of the pdf
s = data.query('country=="Denmark"')
c = s.Q1.value_counts(sort=False, normalize=True) * 100
print(c)

s = data.query('country=="Italy"')
c = s.Q1.value_counts(sort=False, normalize=True) * 100
print(c)

# %%

trust = data.loc[:, 'Q2a':'Q2d']
trust['country'] = data['country']

trust = pandas.melt(trust, id_vars='country')
trust.columns = ['country', 'institute', 'value']

seaborn.barplot(x='institute', y='value', hue='country', data=trust)
pyplot.show()
