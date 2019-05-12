import glob
from pathlib import Path, PurePath
from dash import Dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

p = Path('.')


def Add_Dash(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/dist/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    routes_pathname_prefix='/dashapp/')

    # Override the underlying HTML template
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
                  <a href="/dashapp/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
                </nav>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>'''

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div(
        children=get_datasets(),
        id='dash-container'
      )

    return dash_app.server


def get_datasets():
    """Return previews of all CSVs saved in /data directory."""
    data_filepath = list(p.glob('data/*.csv'))
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
