"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import Flask routes
        from application import routes

        # Import Dash application
        from application.plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        # Compile CSS
        if app.config['FLASK_ENV'] == 'development':
            from application.assets import compile_assets
            compile_assets(app)

        return app
