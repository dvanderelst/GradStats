import pandas
data = pandas.read_csv('raw.csv', sep='\t')


data['major'] = data['major'].str.lower()
data['major'] = data['major'].str.rstrip()

is_engineering = data['major'].str.contains('engineering')
is_engineering[pandas.isna(is_engineering)] = False

data.loc[is_engineering, 'major'] = 'engineering'

# The words at VCL6, VCL9, and VCL12 are not real words

data['check'] = data['VCL6'] + data['VCL9'] + data['VCL12']
print('Before check:' , data.shape)
data = data.query('check == 0')
data = data.query('age < 65')
data = data.query('familysize < 11')
data = data.query('uniquenetworklocation == 1')
print('After check:' , data.shape)

data.to_csv('depression.csv', index=False)


