import pandas
import numpy
#ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NIS/NISPUF14_CODEBOOK.PDF


data = pandas.read_csv('nispuf14.csv')



selected =[
    'PDAT',         # CHILD HAS ADEQUATE PROVIDER DATA
    'EDUC1',        # EDUCATION LEVEL MOTHER
    'INCPOV1',      # POVERTY STATUS
    'FRSTBRN',      # FIRST BORN STATUS
    'SEX',          # GENDER OF CHILD
    'STATE',        # US STATE
    'RACEETHK',     # RACE
    'RACE_K',       # ETHNICITY
    'AGEGRP',       # AGE CATEGORY OF CHILD (19-23, 24-29, 30-35 MO)
    'AGECPOXR',     # AGE IN MONTHS AT CHICKEN POX DISEASE
    'HAD_CPOX',     # CHILD EVER HAD CHICKEN POX DISEASE?
    'ESTIAP14',     #
]

mp = {'UTD':1, 'NOT UTD': 0}

subset = data.loc[:, selected]
subset['mmr'] = data['P_UTDMMX'].map(mp)
subset['hepb'] = data['P_UTDHEP'].map(mp)

#Children need 2 doses of the vaccine at the following ages:
# 12 through 23 months for the first dose.
# 2 through 4 years for the second dose
# (or sooner as long as it's 6 to 18 months after the first dose)

subset['hepa1'] = data['P_UTDHEPA1']
subset['hepa2'] = data['P_UTDHEPA2'].map(mp)

subset['polio'] = data['P_UTDPOL'].map(mp)
subset['hib'] = data['P_UTDHIB'].map(mp)

subset['weight'] = data['PROVWT_D_TERR']

subset.to_csv('vaccinations.csv', index=False)

#%%

## This results in the same results as their online tool
# https://www.cdc.gov/vaccines/imz-managers/coverage/childvaxview/data-reports/mmr/dashboard/2014.html
subset['w_mmr'] = subset['mmr'] * subset['weight']
grp = subset.groupby(['STATE', 'INCPOV1'])
sms = grp.w_mmr.sum()
wgt = grp.weight.sum()



