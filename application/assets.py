from flask_assets import Environment, Bundle


def compile_assets(app):
    """Configure authorization asset bundles."""
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
