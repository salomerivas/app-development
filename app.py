import dash
from dash import dcc, html

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div("Hello, Render!")

# Run the app if this is the main file
if __name__ == "__main__":
    app.run_server(debug=True)
