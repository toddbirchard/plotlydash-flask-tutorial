"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        # Construct the data set
        from . import routes
        from Dash_App import dash_view
        app = dash_view.Add_Dash(app)
        app.register_blueprint(routes.main_bp)

        return app
