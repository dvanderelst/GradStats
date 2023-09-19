from pandas_ods_reader import read_ods
import pandas
import re

path = "wages.ods"

def find(df, pattern, label):
    position = df.Position
    values = position.str.contains(pattern, flags=re.IGNORECASE, regex=True)
    df.Label[values] = label
    return df


# load a sheet based on its index (1 based)
sheet_idx = 1
df = read_ods(path, sheet_idx)

df['Annual Salary'] = df[df.columns[2]].replace('[\$,]', '', regex=True).astype(float)

df['Label'] = 'empty'

find(df, 'Professor', 'Professor')
find(df, 'Asst Professor', 'Asst Professor')
find(df, 'Assoc Professor', 'Assoc Professor')

# Ordered such that the person ends up with the highest label
# if multiple apply

find(df, 'Dean', 'Dean')

find(df, 'Provost', 'Provost')

find(df, 'VP ', 'Vice President')
find(df, 'SVP ', 'Vice President')


# ----

find(df, 'Dir Academic', 'Director Academic')

find(df, 'Coach', 'Coach')
find(df, 'Athletics', 'Athletics')



print(df.Label.value_counts())

data = df.iloc[:,1:]
data = data.query("Label != 'empty'")

data.to_csv('wages.csv', index=None)

#####

grp = data.groupby(['Label'])
mns = grp.median()
print(mns)