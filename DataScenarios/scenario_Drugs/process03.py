import plotly.graph_objects as go
import pandas
import plotly.io as pio




data = pandas.read_csv('drugs.csv')
states = pandas.read_csv('fips.csv', sep='\t')

year=2010
variable='Rates_Alcohol_Binge Past Month_26+'

select = data.query('Year==@year')
select['z'] = select[variable]

df = pandas.merge(select,states, left_on='State', right_on='Name')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'], # Spatial coordinates
    z = df['z'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()