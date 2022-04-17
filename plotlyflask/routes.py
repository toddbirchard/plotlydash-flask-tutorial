"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template, jsonify, make_response, redirect, request


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.jinja2",
        title="Elections",
        description="Elections.",
        template="home-template",
        body="This is a homepage served with Flask.",
    )


@app.route("/api/uploader", methods=['POST'])
def uploader():
    # TODO: check the uploaded file by the security
    f = request.files['file']
    file_name = f.filename
    f.save('data/input.csv')
    return redirect("/dashapp/", code=200)
