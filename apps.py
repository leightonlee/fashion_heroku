#!flask/bin/python
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from app.fashion_routes import create_routes
from app.fashion_store import create_fashion_store

app = Flask(__name__)


def configure_app():
    create_routes(app)
    create_fashion_store(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    app.db = SQLAlchemy(app)


if __name__ == '__main__':
    configure_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
