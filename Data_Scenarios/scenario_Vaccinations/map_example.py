import plotly.graph_objects as go
import pandas
import plotly.io as pio

codes = pandas.read_csv('states.txt',sep='\t')
data = pandas.read_csv('vaccinations.csv')
data = pandas.merge(data, codes, left_on="STATE", right_on='State')

pyplot.figure()`

labels = data.country.values
values = data.percentage.values
popdensity = {}
for l,v in zip(labels, values):
     popdensity[l] = v



pio.renderers.default = "browser"


fig = go.Figure(data=go.Choropleth(
    locations=data.Code, # Spatial coordinates
    z = data.hepb, # Data to be color-coded
    locationmode = "USA-states", # set of locations match entries in `locations`
    colorscale = 'hot',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = 'empty',
    geo_scope='usa', # limit map scope to USA
)

fig.show()
fig.write_image("fig1.pdf")

