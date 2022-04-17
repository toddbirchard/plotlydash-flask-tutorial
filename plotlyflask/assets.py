"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """
    Compile stylesheets if in development mode.

    :param assets: Flask-Assets Environment
    :type assets: Environment
    """
    assets.auto_build = True
    assets.debug = False
    less_bundle = Bundle(
        "less/*.less",
        filters="less,cssmin",
        output="dist/css/styles.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("less_all", less_bundle)
    if app.config["FLASK_ENV"] == "development":
        less_bundle.build()
    return assets
