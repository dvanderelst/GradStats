import pandas
import copy
import string

sheet_names = ['All ages', '0-4', '5-14', '15-29', '30-49', '50-59', '60-69', '70+']
# sheet_names = ['All ages']

statistic_type = 'daly' #daly or yll

data_rows = 215
first_data_column = 8
country_row = 5
iso_row = 6

sex_column = 1
ghe_column = 2

population_persons_row = 8
population_males_row = 226
population_females_row = 444

populations = ['persons', 'males', 'females']

result = pandas.DataFrame()
for sheet_name in sheet_names:

    if statistic_type == 'daly':
        sheet = 'DALYs ' + sheet_name
        read = pandas.read_excel('daly.xlsx', sheet_name=sheet, na_values='.')

    if statistic_type == 'yll':
        sheet = 'YLL ' + sheet_name
        read = pandas.read_excel('yll.xlsx', sheet_name=sheet, na_values='.')

    # %%
    raw = copy.copy(read)
    raw = raw.reset_index()

    for population in populations:
        if population == 'persons': start_row = population_persons_row
        if population == 'males': start_row = population_males_row
        if population == 'females': start_row = population_females_row

        print(sheet_name, population)
        first_data_row = start_row + 1
        last_data_row = population_persons_row + data_rows

        sex_data = raw.iloc[first_data_row:last_data_row + 1, sex_column]
        ghe_data = raw.iloc[first_data_row:last_data_row + 1, ghe_column]
        dta_data = raw.iloc[first_data_row:last_data_row + 1, first_data_column:]
        cnt_data = raw.iloc[country_row, first_data_column:]
        iso_data = raw.iloc[iso_row, first_data_column:]

        per_pop = raw.iloc[population_persons_row, first_data_column:]
        mal_pop = raw.iloc[population_males_row, first_data_column:]
        fem_pop = raw.iloc[population_females_row, first_data_column:]

        iso_data_frame = pandas.DataFrame({'country': cnt_data.values, 'iso': iso_data.values})

        per_data_frame = pandas.DataFrame({'country': cnt_data.values, 'population': per_pop.values})
        mal_data_frame = pandas.DataFrame({'country': cnt_data.values, 'population': mal_pop.values})
        fem_data_frame = pandas.DataFrame({'country': cnt_data.values, 'population': fem_pop.values})

        header = ['sex', 'ghe'] + list(cnt_data.values)
        data = pandas.concat((sex_data, ghe_data, dta_data), axis=1, sort=True)
        data.columns = header

        molten = pandas.melt(data, id_vars=['ghe', 'sex'])
        molten.columns = ['ghe', 'sex', 'country', statistic_type]
        molten['group'] = sheet_name

        # Add population
        if population == 'persons': molten = pandas.merge(molten, per_data_frame, on='country')
        if population == 'males': molten = pandas.merge(molten, mal_data_frame, on='country')
        if population == 'females': molten = pandas.merge(molten, fem_data_frame, on='country')

        result = pandas.concat((result, molten))

result = pandas.merge(result, iso_data_frame, on='country')
result['normalized_pm'] = (result[statistic_type] / result['population']) * 1000000
result.to_csv(statistic_type+'.csv', index=False, na_rep='NA')