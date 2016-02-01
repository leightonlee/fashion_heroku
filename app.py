import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from fashion_heroku.controller.fashion_routes import create_routes
from fashion_heroku.store.fashion_store import create_fashion_store

app = None


def create_app():
    app = Flask(__name__)
    create_routes(app)
    create_fashion_store(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    app.db = SQLAlchemy(app)
    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
