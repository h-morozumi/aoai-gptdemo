import importlib

import flask

import blueprints


def create_app():
    app = flask.Flask(__name__)

    for blueprint in blueprints.all_blueprints:
        importlib.import_module(blueprint.import_name)
        app.register_blueprint(blueprint)

    return app