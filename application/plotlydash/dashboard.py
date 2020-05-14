"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from .layout import html_layout


def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(server=server,
                         routes_pathname_prefix='/dashapp/',
                         external_stylesheets=[
                             '/static/dist/css/styles.css',
                             'https://fonts.googleapis.com/css?family=Lato'
                             ]
                         )

    # Prepare a DataFrame
    df = pd.read_csv('data/311-calls.csv', parse_dates=['created_date'])
    df['created_date'] = df['created_date'].dt.date
    num_complaints = df['complaint_type'].value_counts()
    to_remove = num_complaints[num_complaints <= 20].index
    df.replace(to_remove, np.nan, inplace=True)

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
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
                    'height': 500,
                    'padding': 150
                }
            }),
            create_data_table(df)
            ],
        id='dash-container'
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id='database-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
        sort_mode='native',
        page_size=300
    )
    return table
