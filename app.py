#!flask/bin/python
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from fashion_routes import create_routes
from fashion_store import create_fashion_store

app = Flask(__name__)
db = SQLAlchemy(app)


def configure_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
    create_routes(app)
    create_fashion_store(app)
    app.db = SQLAlchemy(app)


if __name__ == '__main__':
    configure_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
