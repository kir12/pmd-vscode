import os

from flask import Flask, request
from flask_jsonrpc import JSONRPC

# consider replacement at https://github.com/openlawlibrary/pygls

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    jsonrpc = JSONRPC(app, "/", enable_web_browsable_api=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @jsonrpc.method("App.index")
    def hello() -> str:
        print("test")
        return 'Hello, World!'

    @jsonrpc.method("initialize")
    def hello() -> str:
        print(request.data)
        return 'Hello, World!'

    return app