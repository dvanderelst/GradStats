import pandas

# pip install savreaderwriter
import savReaderWriter as spss

filename = 'data.sav'

raw_data = spss.SavReader(filename, returnHeader = True, ioUtf8=True)
raw_data_list = list(raw_data)
df = pandas.DataFrame(raw_data_list)

header = df.iloc[0,:]
data = df.iloc[1:,:]
data.columns = header

data.to_csv('science.csv', index=False)

#%%


grp = data.groupby(['q16', 'q20f1'])
cnts = grp.weight.sum()
cnts = cnts.reset_index()
print(cnts)
tab = cnts.pivot(index='q20f1',columns='q16', values='weight')
#tab = tab.iloc[:-1,:-1]

for i in range(3):
    tab.iloc[:,i] = tab.iloc[:,i] / tab.iloc[:,i].sum()

print(tab)