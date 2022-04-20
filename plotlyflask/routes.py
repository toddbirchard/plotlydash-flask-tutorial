"""Routes for parent Flask app."""
import json
import pandas as pd
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
    f.save('data/input.csv')
    return redirect("/dashapp/", code=200)


# the mockup of results

@app.route("/api/winner", methods=['GET'])
def get_winner():
    winner = pd.read_csv("data/winner.csv", sep=';')
    data = {
        'message': 'The winner is...',
        'status': 200,
        'data': json.loads(winner.to_json())
    }
    return make_response(jsonify(data))