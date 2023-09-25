import pandas
from matplotlib import pyplot

from ClassPackage import mapping


data = pandas.read_csv('overdoses.csv')

# %%

pyplot.style.use('ggplot')

pyplot.figure(figsize=(10, 5))
pyplot.subplot(1, 2, 1)
cnt = data.HOUR.value_counts(sort=False)
pyplot.plot(cnt.index, cnt)
pyplot.xlabel('Hour')
pyplot.ylabel('Responses')
pyplot.title('Reponses as a function of time of day')

pyplot.subplot(1, 2, 2)
cnt = data.MONTH.value_counts(sort=False)
pyplot.plot(cnt.index, cnt)
pyplot.xticks(rotation=60)
pyplot.xlabel('Month')
pyplot.ylabel('Responses')
pyplot.title('Reponses as a function of month')
pyplot.show()

# %%
n = 10

pyplot.figure()
cnt = data.NEIGHBORHOOD.value_counts()
top = cnt.head(n)
pyplot.bar(range(n), top)
pyplot.xticks(range(n), top.index, rotation=90)
pyplot.title(str(n) + ' most frequent neighborhoods')
pyplot.ylabel('Responses')
pyplot.show()

# %%
cincy = mapping.Cincinnati()
cincy.plot()
pyplot.scatter(data.LONGITUDE_X, data.LATITUDE_X, alpha=0.5, s=3)
pyplot.show()
