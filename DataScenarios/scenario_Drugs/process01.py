# https://think.cs.vt.edu/corgis/python/drugs/drugs.html
import pandas
from matplotlib import pyplot
import matplotlib


import stats

pyplot.style.use('default')
pyplot.style.use('seaborn-deep')
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['font.sans-serif'] = "NotoSans"
data = pandas.read_csv('drugs.csv')

pyplot.scatter(data.Year,data.Year)
pyplot.show()

import matplotlib.font_manager
matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')


fonts = []
for f in matplotlib.font_manager.fontManager.afmlist: fonts.append(f.name)
for f in matplotlib.font_manager.fontManager.ttflist: fonts.append(f.name)
fonts = set(fonts)