#!flask/bin/python
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from fashion_routes import create_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)


def configure_app():
    create_routes(app)


if __name__ == '__main__':
    configure_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
