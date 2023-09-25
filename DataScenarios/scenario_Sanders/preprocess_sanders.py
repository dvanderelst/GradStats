import pandas
import copy

# expenditure
read2 = pandas.read_excel('expenditure.xls', sheet_name='Sheet2', na_values='.')
read3 = pandas.read_excel('expenditure.xls', sheet_name='Sheet3', na_values='.')

read2 = read2.iloc[:, [1, 2, 3, 5]]
read2.columns = ['year', 'region', 'code', 'expenditure']

read2['country'] = read3.iloc[:, 3]

# hale
expect = pandas.read_excel('expect.xls', sheet_name='Sheet2', na_values='.')
expect = expect.iloc[:, [1, 2, 3, 4, 6,9,11]]

# life ex. at birth
# healthy life exp
# life exp. at 60
expect.columns = ['year', 'region', 'code', 'sex', 'atbirth', 'hale', 'at60']

merged = pandas.merge(read2, expect, on=['year', 'region', 'code'])

merged.to_csv('sanders.csv', index=False)

print(read2.head())
print(expect.head())