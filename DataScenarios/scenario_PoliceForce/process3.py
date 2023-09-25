import numpy
import pandas
from matplotlib import pyplot

data = pandas.read_csv('PoliceForce.csv', parse_dates=['INCIDENT_DATE'])
data['gender'] = 'OTHER'
data['gender'][data['SUBJECT_GENDER']=='MALE'] = 'MALE'
data['gender'][data['SUBJECT_GENDER']=='FEMALE'] = 'FEMALE'

label = 'CHEMICAL IRRITANT'
variable = 'SUBJECT_RACE'

selected_data = data.query('INCIDENT_DESCRIPTION == @label')


grp_selected = selected_data.groupby(variable)
cnt_selected = grp_selected.count()
cnt_selected = cnt_selected.reset_index()

grp_all = data.groupby(variable)
cnt_all = grp_all.count()
cnt_all = cnt_all.reset_index()

normed = cnt_selected.INCIDENT_NO / cnt_all.INCIDENT_NO

n = normed.size

pyplot.bar(range(n),normed)
pyplot.xticks(range(n), cnt_all[variable])
pyplot.show()
