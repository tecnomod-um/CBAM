import json

from flask import Flask

from endpoint import Config

from endpoint.JsonEncoder import DateTimeEncoder
from endpoint.RestEndpoint import main_blueprint


def create_app():
    app = Flask(__name__)
    app.json_encoder = DateTimeEncoder
    app.register_blueprint(main_blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
