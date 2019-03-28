from flask import Flask
from . import dash_view


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    dash_app = dash_view.Add_Dash(app)

    with app.app_context():

        # Construct the data set
        from . import routes
        app.register_blueprint(routes.main_bp)

        return app
