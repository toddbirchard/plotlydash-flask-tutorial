from flask import Flask
from . import plotly_dash_views


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    dash_app = plotly_dash_views.dataframes.Add_Dash(app)

    with app.app_context():

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_bp)
        # app.register_blueprint(plotly_dash_views.routes.plotly_bp)

        return app
