from dash import html

def navbar():
    return html.Nav([
        html.Ul([
            html.Li(html.A("Home", href="/")),
            html.Li(html.A("Graphiques", href="/graphs")),
            html.Li(html.A("Carte", href="/map")),
            html.Li(html.A("informations", href="/description")),

        ], className="nav-list"),
    ], className="navbar")
