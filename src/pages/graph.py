import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output
from src.components.xyRange import xyRangeChoiser


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
        dcc.Graph(id="dynamic-graph"),

        html.P("Catégories",style={"text-align":"center"}),
        # Radio button group
        dcc.RadioItems(
            id='radio-selector',
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'ABC', 'value': 'ABC'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'E', 'value': 'E'},

            ],
            value='A',  # Default value
            inline=True, 
            style={"text-align":"center"}
        ),
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
        Input("y-max", "value"),
        Input('radio-selector', 'value')
        ]
    )
    # Choose the dataset based on the selection

    def update_graph(graph_type, x_min, x_max, y_min, y_max,categorie):

        if categorie in ["A","ABC","B","C","D","E"]:
            data=pd.read_json("data/cleaned/listSommecat_"+categorie+".json") # récupération de la donnée en fonction de la catégorie 
        #is_categorical = pd.api.types.is_categorical_dtype(data["periodes"]) or data["periodes"].dtype == object
        if graph_type == "histogram":
             fig=px.bar(data, x="periodes", y="nombre_demandeur_emploi", title="Histogramme", height=600,)
        elif graph_type == "line":
             fig= px.line(data, x="periodes", y="nombre_demandeur_emploi", title="Courbe", height=600)
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',  # Ensure all ticks are displayed
                tickangle=-45,      # Rotate x-axis labels for better readability
                title="Période"
            ),
            yaxis=dict(
                title="Nombre de demandeurs d'emploi"
            ),
            template="plotly_white"  # Optional for a clean style
        )

                # Apply axis limits
        # Handle categorical and numerical axes dynamically
        # x_axis_range = None
        # if not is_categorical:
        #     x_axis_range = [x_min, x_max] if x_min is not None and x_max is not None else None

        # y_axis_range = [y_min, y_max] if y_min is not None and y_max is not None else None

        # # Update the layout with dynamic ranges
        # fig.update_layout(
        #     xaxis=dict(
        #         range=x_axis_range,
        #         categoryorder="array" if is_categorical else None,
        #         categoryarray=[x_min, x_max] if is_categorical and x_min and x_max else None
        #     ),
        #     yaxis=dict(range=y_axis_range)
        # )
        return fig

    return app.layout
