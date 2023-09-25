import quandl
import pandas
from matplotlib import pyplot


# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - Cincinnati, OH
data = quandl.get("ZILLOW/M26_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data.columns = ['cin']

# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - Columbus, OH
data2 = quandl.get("ZILLOW/M28_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data['col'] = data2['Value']

# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - Columbus, OH
data3 = quandl.get("ZILLOW/M362_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data['cle'] = data3['Value']

# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - Boston, MA
data4 = quandl.get("ZILLOW/M10_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data['bos'] = data4['Value']

# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - Seattle, QA
data5 = quandl.get("ZILLOW/M15_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data['sea'] = data5['Value']

# Zillow Home Value Index (Metro): Median Listing Price - Two Bedrooms - New York
data6 = quandl.get("ZILLOW/M2_MLP2B", authtoken="NM55D4TthA7TzoF5NbYf")
data['new'] = data6['Value']


#pyplot.plot(data)
#pyplot.show()


index = data.index
index = index.to_series()
times = pandas.to_datetime(index)

data['time'] = times
data['month'] = times.dt.month_name()
data['month_nr'] = times.dt.month
data['year'] = times.dt.year

data = data.reset_index()
data = data.drop('Date', axis=1)

data.to_csv('real_estate.csv', index=False)