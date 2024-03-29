"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, request


@app.route("/")
def home():
    """Home page of Flask Application."""
    return render_template(
        "index.jinja2",
        title="Plotly Dash Flask Tutorial",
        description="Embed Plotly Dash into your Flask applications.",
        template="home-template",
        body="This is a homepage served with Flask.",
        base_url=request.base_url,
    )
