from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='secretsecret',
        #Put your database config here if any.
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # ++++++++++++++++++++++to avoid keys sorted ascending++++++++++++++++++++
    app.config['JSON_SORT_KEYS'] = False

    from . import auth
    app.register_blueprint(auth.bp)

    from . import maintenance
    app.register_blueprint(maintenance.bp)
    app.add_url_rule('/', endpoint='index')

    return app