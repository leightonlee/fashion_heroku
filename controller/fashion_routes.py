from flask import send_file, jsonify, render_template
import os
from random import randint
from requests import codes

from fashion_heroku.store.fashion_store import get_fashion_items
import fashion_heroku.img as IMAGES


def validate(page):
    value = int(page)
    if value <= 0:
        raise ValueError
    return value


def create_routes(app):
    """
    Create routes for fashion flask app
    """
    @app.route('/', methods=["GET"])
    def home():
        """
        Gets the home page
        """
        return render_template("index.html")

    @app.route('/fashion/<page>', methods=["GET"])
    def get_fashion_tips(page):
        """
        Gets a list of fashion items
        """
        try:
            # validates the page
            validated_page = validate(page)
            # gets the list of fashion items for the page
            items = get_fashion_items(validated_page, 20)
            # randomizes the page of items
            random_list = randomize_list(items)
        except ValueError:
            return "BAD REQUEST", codes.BAD_REQUEST

        return jsonify(items=random_list), codes.ok

    @app.route('/fashion/image/<image_name>', methods=["GET"])
    def get_image(image_name):
        """
        Gets an image for a fashion item
        """
        # gets the path of the image in the images folder
        image_path = os.path.join(os.path.dirname(IMAGES.__file__), image_name)
        # verifies that the image exists
        if not os.path.isfile(image_path):
            return None, codes.not_found
        # sends the image
        return send_file(image_path), codes.ok


def randomize_list(items):
    """
    Randomizes the list
    """
    random_list = []
    while items:
        random_list.append(items.pop(randint(0, len(items) - 1)))
    return random_list

