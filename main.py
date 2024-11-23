from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import src.components.navbar as navbar
from src.pages.home import home_page
from src.pages.graph import graph_page , register_callbacks
from src.pages.geoLoc import map_page
from src.components.footer import footer
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "WStatAnalyser"

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar.navbar(),
    html.Div(id="page-content"),
    footer()
])
# Register callbacks
register_callbacks(app)

# Callbacks pour le routage
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/graphs":
        return graph_page()
    elif pathname == "/map":
        return map_page()
    else:
        return home_page()

if __name__ == "__main__":
    app.run_server(debug=True)
