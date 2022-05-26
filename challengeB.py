import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output


# Creating the App
app = Dash(__name__)


# Import and Clean Data
df = pd.read_csv('intro_bees.csv')
df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace = True)


# App Layout
app.layout = html.Div([

    html.H1('Web Application Dashboards with Dash', style = {'text-align': 'center'}),

    dcc.Dropdown(id = 'slct_cause',
                 options = [
                     {"label": "Disease", "value": "Disease"},
                     {"label": "Other", "value": "Other"},
                     {"label": "Pesticides", "value": "Pesticides"},
                     {"label": "Pests_excl_Varroa", "value": "Pests_excl_Varroa"},
                     {"label": "Unknown", "value": "Unknown"},
                     {"label": "Varroa_mites", "value": "Unknown"}],
                 multi=False,
                 value="Disease",
                 style={'width': "40%"}
                 ),

    html.Div(id = 'output_container', children = []),
    html.Br(),

    dcc.Graph(id = 'my_bee_map', figure = {})

])


# Connect the Plotly
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_cause', component_property='value')]
)
def update_graph(option_slctd):

    container = "The cause chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Affected by"] == option_slctd]
    dff = dff[(dff["State"] == "Idaho") | (dff["State"] == "New York") | (dff["State"] == "New Mexico")]

    # Plotly Express
    fig = px.line(
        data_frame=dff,
        x = 'Year',
        y = 'Pct of Colonies Impacted',
        color = 'State'
    )


    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

