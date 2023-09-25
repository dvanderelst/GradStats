from pandas_ods_reader import read_ods
import pandas

sheet_idx = 1
fips = read_ods('fips.ods', sheet_idx)

data = pandas.read_csv('cty_covariates.csv')

# Some cityzones span multiple counties and are
# listed multiple times. I average across those county
# listings to obtain a single estimate per CZ.
# This does not take into account differences in pop between
# county parts of a CZ

by_city_zone = data.groupby(['czname'])
by_city_zone = by_city_zone.mean()
by_city_zone = by_city_zone.reset_index()

data = pandas.merge(by_city_zone, fips, on='state')

data.to_csv('city_zones.csv', index=False)
