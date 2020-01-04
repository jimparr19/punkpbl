from dash.dependencies import Input, Output
from main import app


@app.callback(
    Output("hidden_data", "value"),
    [
        Input("switches_input", "value"),
    ]
)
def update_hidden_data(switches_value):
    data = dict()
    data['punk_index'] = switches_value
    return data
