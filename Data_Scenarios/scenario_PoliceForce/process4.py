import numpy
import pandas

data = pandas.read_csv('PoliceForce.csv', parse_dates=['INCIDENT_DATE'])

# generate 3 gender classes
data['gender'] = 'OTHER'
data['gender'][data['SUBJECT_GENDER']=='MALE'] = 'MALE'
data['gender'][data['SUBJECT_GENDER']=='FEMALE'] = 'FEMALE'

# add 5 year bands
dates = data['INCIDENT_DATE']
year = dates.dt.year
data['year'] = year
data['round'] = numpy.floor(data['year']/5) * 5

grp = data.groupby(['round','gender','INCIDENT_DESCRIPTION'])
cnt = grp.count()
cnt = cnt.reset_index()

pyplot.xlim([0, 100000])


subset = data.loc[:,['INCIDENT_DESCRIPTION','OFFICER_GENDER']]
subset = subset.query('INCIDENT_DESCRIPTION == "WEAPON DISCHARGE AT AN ANIMAL"')

grp = subset.groupby('OFFICER_GENDER')
cnt = grp.count()
cnt = cnt.reset_index()
