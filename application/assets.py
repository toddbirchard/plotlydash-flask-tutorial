from flask_assets import Environment, Bundle


def compile_assets(app):
    """Compile stylesheets if `app` is running in development mode."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    less_bundle = Bundle('less/*.less',
                         filters='less,cssmin',
                         output='dist/css/styles.css',
                         extra={'rel': 'stylesheet/less'})
    assets.register('less_all', less_bundle)
    less_bundle.build(force=True)
