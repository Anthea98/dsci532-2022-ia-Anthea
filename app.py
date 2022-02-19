from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd

# Read in global data
# Read in global data
athlete = pd.read_csv("olympics.csv")

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
    html.Iframe(
        id='histogram',
        style={'border-width': '0', 'width': '100%', 'height': '500px'}),
    dcc.Dropdown(
        id='diff_medal',
        value="Gold",  # REQUIRED to show the plot on the first page load
        options=[{'label': medal, 'value': medal} for medal in ["Gold","Silver","Bronze"]])])

# Set up callbacks/backend
@app.callback(
    Output('histogram', 'srcDoc'),
    Input('diff_medal', 'value'))
def plot_altair(medal):
    alt.data_transformers.disable_max_rows()
    chart = alt.Chart(athlete[athlete["medal"]==medal]).mark_bar().encode(
        x=alt.X("height",bin=True),
        y='count()',
        tooltip='height').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)