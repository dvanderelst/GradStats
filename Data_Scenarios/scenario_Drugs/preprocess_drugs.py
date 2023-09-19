from course import corgis

import drugs
data = drugs.get_reports()
data = corgis.data2frame(data)
data.to_csv('drugs.csv',index=False)
