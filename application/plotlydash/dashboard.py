"""Create a Dash app within a Flask app."""
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from .layout import html_layout


def create_dashboard(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/dist/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    dash_app = dash.Dash(server=server,
                         external_stylesheets=external_stylesheets,
                         external_scripts=external_scripts,
                         routes_pathname_prefix='/dashapp/')

    # Prepare a DataFrame
    df = pd.read_csv('data/311-calls.csv')
    num_complaints = df['complaint_type'].value_counts()
    to_remove = num_complaints[num_complaints <= 20].index
    df.replace(to_remove, np.nan, inplace=True)

    # Override the underlying HTML template
    dash_app.index_string = html_layout

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div(
        children=[dcc.Graph(
            id='histogram-graph',
            figure={
                'data': [
                    {
                        'x': df['complaint_type'],
                        'text': df['complaint_type'],
                        'customdata': df['unique_key'],
                        'name': '311 Calls by region.',
                        'type': 'histogram'
                    }
                ],
                'layout': {
                    'title': 'NYC 311 Calls category.',
                    'height': 600,
                    'padding': 150
                }
            }),
            create_data_table(df)
            ],
        id='dash-container'
    )

    return dash_app.server


def create_data_table(df):
    """Create table from Pandas DataFrame."""
    table_preview = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table_preview
