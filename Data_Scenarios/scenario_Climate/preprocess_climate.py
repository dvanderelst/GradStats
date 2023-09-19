import pandas

#%% CO2
co2 = pandas.read_excel('co2.xls', sheet_name= 'Data')
melt_co2 = pandas.melt(co2, id_vars=['Country Name', 'Country Code'])
melt_co2.columns = ['country', 'iso', 'year', 'co2']

#%% Forest
forest = pandas.read_excel('forest.xls', sheet_name= 'Data')
melt_forest = pandas.melt(forest, id_vars=['Country Name', 'Country Code'])
melt_forest.columns = ['country', 'iso', 'year', 'forest']

#%% renawable
renewable = pandas.read_excel('renewable.xls', sheet_name= 'Data')
melt_renewable = pandas.melt(renewable, id_vars=['Country Name', 'Country Code'])
melt_renewable.columns = ['country', 'iso', 'year', 'renewable']

#%% growth
growth = pandas.read_excel('growth.xls', sheet_name= 'Data')
melt_growth = pandas.melt(growth, id_vars=['Country Name', 'Country Code'])
melt_growth.columns = ['country', 'iso', 'year', 'growth']

#%% population
population = pandas.read_excel('population.xls', sheet_name= 'Data')
melt_population = pandas.melt(population, id_vars=['Country Name', 'Country Code'])
melt_population.columns = ['country', 'iso', 'year', 'population']

#%%
merged = pandas.merge(melt_forest, melt_co2, on=['country','iso', 'year'])
merged = pandas.merge(merged, melt_renewable, on=['country','iso', 'year'])
merged = pandas.merge(merged, melt_growth, on=['country','iso', 'year'])
merged = pandas.merge(merged, melt_population, on=['country','iso', 'year'])

merged.to_csv('climate.csv', index=False)