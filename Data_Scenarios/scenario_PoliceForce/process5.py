import numpy
import pandas
import seaborn
from matplotlib import pyplot

data = pandas.read_csv('PoliceForce.csv', parse_dates=['INCIDENT_DATE'])


dates = data['INCIDENT_DATE']
year = dates.dt.year
data['year'] = year

# generate 3 gender classes
data['gender'] = 'OTHER'
data['gender'][data['SUBJECT_GENDER']=='MALE'] = 'MALE'
data['gender'][data['SUBJECT_GENDER']=='FEMALE'] = 'FEMALE'
data = data.query("gender != 'OTHER'")

#data = data.query('INCIDENT_TYPE == 9823')

selected = ['OTHER', 'HISPANIC/LATINO']
data1 = data.query('SUBJECT_RACE in @selected')
data2 = data.query('SUBJECT_RACE not in @selected')

grp = data.groupby(['gender'])
cnt = grp.count()
cnt = cnt.reset_index()

pyplot.bar(['Female', 'Male'], cnt.CASE_NO, color=['red', 'green'])
pyplot.show()


