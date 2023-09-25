import pandas

# pip install savreaderwriter
import savReaderWriter as spss

filename = 'pew2013lgbtpublicdatarelease.sav'

raw_data = spss.SavReader(filename, returnHeader = True, ioUtf8=True)
raw_data_list = list(raw_data)
df = pandas.DataFrame(raw_data_list)

header = df.iloc[0,:]
data = df.iloc[1:,:]
data.columns = header

data.to_csv('lbtq.csv', index=False)