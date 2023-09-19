import plotly.graph_objects as go
import pandas
import plotly.io as pio


pio.renderers.default = "browser"

#['plotly_mimetype', 'jupyterlab', 'nteract', 'vscode',
#         'notebook', 'notebook_connected', 'kaggle', 'azure', 'colab',
#         'cocalc', 'databricks', 'json', 'png', 'jpeg', 'jpg', 'svg',
#         'pdf', 'browser', 'firefox', 'chrome', 'chromium', 'iframe',
#         'iframe_connected', 'sphinx_gallery']

data = pandas.read_csv('drugs.csv')
states = pandas.read_csv('fips.csv', sep='\t')

year=2012
variable='Rates_Alcohol_Binge Past Month_26+'

select = data.query('Year==@year')
select['z'] = select[variable]

df = pandas.merge(select,states, left_on='State', right_on='Name')

fig = go.Figure(data=go.Choropleth(
    locations=df['Code'], # Spatial coordinates
    z = df['z'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Spectral',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = variable,
    geo_scope='africa', # limite map scope to USA
)

fig.show()
fig.write_image("fig1.pdf")

