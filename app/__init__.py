from flask import Flask
from app.db import db_session


def create_app():
    app = Flask(__name__)

    from app.api.routes import blueprint as api

    app.register_blueprint(api, url_prefix='/api/1')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
        
    return app
