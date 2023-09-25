from course import corgis

import health
data = health.get_all_reports()
data = corgis.data2frame(data)
data.to_csv('health.csv',index=False)
