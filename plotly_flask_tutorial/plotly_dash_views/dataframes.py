import glob
from pathlib import Path, PurePath
from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

p = Path('.')


def Add_Dash(server):
    """Populates page with previews of datasets."""
    external_stylesheets = ['https://hackers.nyc3.cdn.digitaloceanspaces.com/css/plotly-flask-tutorial8.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    dash_app = Dash(server=server,
                    url_base_pathname='/plotly_dash_views/',
                    external_stylesheets=external_stylesheets)
    dash_app.index_string = '''<!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
            </head>
            <body>
                <nav>
                  <a href="/"><i class="fas fa-home"></i> Home</a>
                  <a href="/plotly_dash_views/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
                </nav>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>'''


    # Create layout
    dash_app.layout = html.Div(
        children=get_datasets(),
        id='flex-container'
      )

    return dash_app.server


def get_datasets():
    """Gets all CSVs in /data directory."""
    data_filepath = list(p.glob('plotly_flask_tutorial/plotly_dash_views/data/*.csv'))
    arr = ['This is an example Plot.ly Dash App.']
    for index, csv in enumerate(data_filepath):
        print(PurePath(csv))
        df = pd.read_csv(data_filepath[index]).head(10)
        table_preview = dash_table.DataTable(
            id='table_' + str(index),
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            sorting=True,
        )
        arr.append(table_preview)
    return arr
