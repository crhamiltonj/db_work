from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api.routes import blueprint as api

    app.register_blueprint(api, url_prefix='/api/1')
    return app
