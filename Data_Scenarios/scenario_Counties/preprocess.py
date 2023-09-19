from course import corgis

import county_demographics
data = county_demographics.get_all_counties()
data = corgis.data2frame(data)
data.to_csv('counties.csv',index=False)
