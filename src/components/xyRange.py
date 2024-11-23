from dash import html ,dcc
# Input fields for axis limits
# 

def  xyRangeChoiser():
    
    return   html.Div([
                        html.Div([
                            html.Label("X-Axis Min"),
                            dcc.Input(id="x-min", type="text", placeholder="Min X", style={"width": "100px"})
                        ], style={"display": "inline-block", "margin-right": "20px"}),

                        html.Div([
                            html.Label("X-Axis Max"),
                            dcc.Input(id="x-max", type="text", placeholder="Max X", style={"width": "100px"})
                        ], style={"display": "inline-block", "margin-right": "20px"}),

                        html.Div([
                            html.Label("Y-Axis Min"),
                            dcc.Input(id="y-min", type="number", placeholder="Min Y", style={"width": "100px"})
                        ], style={"display": "inline-block", "margin-right": "20px"}),

                        html.Div([
                            html.Label("Y-Axis Max"),
                            dcc.Input(id="y-max", type="number", placeholder="Max Y", style={"width": "100px"})
                        ], style={"display": "inline-block"})
                    ], style={"text-align": "center", "margin": "20px"})

     