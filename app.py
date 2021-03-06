import os
from random import randint

from flask import Flask, jsonify, render_template, send_file
from flask.ext.sqlalchemy import SQLAlchemy
from requests import codes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)


class FashionItem(db.Model):
    """
    Model for a fashion item.
    """
    __tablename__ = 'FashionItem'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    blurb = db.Column(db.String(1000))
    author = db.Column(db.String(200))
    thumbnail_url = db.Column(db.String(200))
    details_url = db.Column(db.String(200))

    def __init__(self,
                 title,
                 blurb,
                 author,
                 thumbnail_url,
                 details_url):
        self.title = title
        self.blurb = blurb
        self.author = author
        self.thumbnail_url = thumbnail_url
        self.details_url = details_url

    def to_dict(self):
        return {
            "title": self.title,
            "blurb": self.max_word_count(self.blurb, 32),
            "author": self.author,
            "thumbnail_url": self.thumbnail_url,
            "details_url": self.details_url,
            }

    def max_word_count(self, sentence, max_count):
        """
        Returns a sentence with at most max_count words
        """
        indexes = [i for i, char in enumerate(sentence) if char == " "]
        if len(indexes) >= max_count:
            return sentence[:indexes[max_count-1]]
        return sentence

    def __repr__(self):
        return '<title %r>' % self.title



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
    image_path = app.root_path + '/static/img/' + image_name
    try:
        return send_file(image_path), codes.ok
    except:
        # Unable to get the file. Sending a not found image instead.
        return send_file(app.root_path + '/static/img/not-found.png'), codes.not_found


def validate(page):
    """
    Validates that the page is greater than 0
    """
    value = int(page)
    if value <= 0:
        raise ValueError
    return value


def get_fashion_items(page, items_per_page):
    """
    Retrieves a list of fashion items from the db
    :param page: Page of items
    :param items_per_page: number of items per page
    :return: List of fashion items
    """
    # Gets a subset of fashion items based on the page and items per page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    items = FashionItem.query.order_by(FashionItem.id)[start_index:end_index]
    return [item.to_dict() for item in items]


def randomize_list(items):
    """
    Randomizes the list
    """
    random_list = []
    while items:
        random_list.append(items.pop(randint(0, len(items) - 1)))
    return random_list


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
