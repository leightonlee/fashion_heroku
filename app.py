import os

from project import app
from project.routes import create_routes


if __name__ == '__main__':
    create_routes(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
