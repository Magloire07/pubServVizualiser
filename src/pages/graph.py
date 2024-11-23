import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output
from src.components.xyRange import xyRangeChoiser

# Exemple de données
data = pd.DataFrame({
    "Catégories": ["A", "B", "C", "D"],
    "Valeurs": [10, 20, 15, 25]
})

# Fonction pour créer un layout de page dynamique
def graph_page():
    return html.Div([
        html.H1("Visualisez et analysez", style={"text-align": "center" , "margin-bottom":40}),
        html.P("veillez choisir  le type d'affichage dans le menu déroulant",style={"text-align": "center"}),
        dcc.Dropdown(
            id="graph-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",  # Valeur par défaut
            style={"width": "50%", "margin": "auto", "margin-bottom":40}
        ),
        xyRangeChoiser(),
        dcc.Graph(id="dynamic-graph")
    ],className="page-content")
    
    # Callback pour mettre à jour le graphique
def register_callbacks(app):
    @app.callback(
        Output("dynamic-graph", "figure"),
        [
        Input("graph-selector", "value"),
        Input("x-min", "value"),
        Input("x-max", "value"),
        Input("y-min", "value"),
        Input("y-max", "value")
        ]
    )
    def update_graph(graph_type, x_min, x_max, y_min, y_max):

        is_categorical = pd.api.types.is_categorical_dtype(data["Catégories"]) or data["Catégories"].dtype == object
        if graph_type == "histogram":
             fig=px.bar(data, x="Catégories", y="Valeurs", title="Histogramme", height=600)
        elif graph_type == "line":
             fig= px.line(data, x="Catégories", y="Valeurs", title="Courbe", height=600)
                # Apply axis limits
        # Handle categorical and numerical axes dynamically
        x_axis_range = None
        if not is_categorical:
            x_axis_range = [x_min, x_max] if x_min is not None and x_max is not None else None

        y_axis_range = [y_min, y_max] if y_min is not None and y_max is not None else None

        # Update the layout with dynamic ranges
        fig.update_layout(
            xaxis=dict(
                range=x_axis_range,
                categoryorder="array" if is_categorical else None,
                categoryarray=[x_min, x_max] if is_categorical and x_min and x_max else None
            ),
            yaxis=dict(range=y_axis_range)
        )
        return fig

    return app.layout
