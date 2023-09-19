from pandas_ods_reader import read_ods
import pandas
import seaborn
from matplotlib import pyplot

for income_concept in ['ind', 'fam']:
    data = read_ods('table3_absmob_by_cohort_parpctile_gnd.ods', 1)
    cohort = data['cohort']
    pattern = 'abs_mob_pos_par_.*_' + income_concept + '_p.*'
    data = data.filter(regex=(pattern))
    data['cohort'] = cohort

    data = pandas.melt(data, id_vars='cohort')

    data['percentile'] = data.variable.str.extract(r'(\d+)')
    data['gender'] = data.variable.str.extract(r'_f(.)_')
    data['gender'] = data['gender'].replace('d', 'f')
    data['gender'] = data['gender'].replace('s', 'm')

    data = data.iloc[:, [0, 2, 3, 4]]

    data['percentile'] = pandas.to_numeric(data['percentile'])

    data.columns = ['cohort', 'prob', 'percentile', 'gender']

    data.to_csv('mobility_' + income_concept + '.csv', index=False)

    ##
    grp = data.groupby(['cohort', 'gender'])
    grp = grp.mean()
    grp = grp.reset_index()

    seaborn.lineplot(x='cohort', y='prob', hue='gender', data=grp)
    pyplot.show()
