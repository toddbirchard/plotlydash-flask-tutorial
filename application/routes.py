"""Routes for core Flask app."""
import os
from flask import Blueprint, render_template
from flask_assets import Environment, Bundle
from flask import current_app as app

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
assets = Environment(app)
Environment.auto_build = True
Environment.debug = False
less_bundle = Bundle('less/*.less',
                     filters='less,cssmin',
                     output='dist/css/styles.css',
                     extra={'rel': 'stylesheet/less'})
js_bundle = Bundle('js/*.js',
                   filters='jsmin',
                   output='dist/js/main.js')
assets.register('less_all', less_bundle)
assets.register('js_all', js_bundle)
if app.config['FLASK_ENV'] == 'development':
    less_bundle.build(force=True)
    js_bundle.build()


@main_bp.route('/')
def home():
    """Landing page."""
    return render_template('index.html',
                           title='Plotly Flask Tutorial.',
                           template='home-template',
                           body="This is an example homepage served with Flask.")
