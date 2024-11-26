import os
import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div("Hello, Render!")

if __name__ == "__main__":
    # Use the PORT environment variable Render provides or default to 8050 for local testing
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port, debug=False)
