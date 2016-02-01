from project import db
from project.models import FashionItem


def populate_db():
    """
    Populates the db with some data
    :return:
    """
    db.session.add(FashionItem(
        "Hat",
        "It's a hat dude. What more do you want",
        "Hat Man",
        "pikachu.png",
        "http://HatsOwnYou.com"))
    # Populates a fashion item entry with a non-existing picture
    db.session.add(FashionItem(
        "Glove",
        "It keeps your hands warm and looks pretty. What else do you want?",
        "Glove Girl",
        "non-existent.png",
        "http://GlovesForGirls.com"))
    # Populates a fashion item entry with more than 32 words in the blurb
    db.session.add(FashionItem(
        "Scarf",
        "Scarves are super warm. You will want to always have a scarf on you. "
        "If you don't have a scarf, you should buy one now. PLEASE BUY ONE NOW! "
        "IF YOU DON'T, I will be very sad.",
        "Scarf Stranger",
        "pikachu.png",
        "http://www.StrangeScarves.com"))

    generic_items = create_accessories(110)
    for item in generic_items:
        db.session.add(item)
    db.session.commit()


def add_fashion_item(item):
    db.session.add(item)


def create_accessories(count):
    """
    Creates a large number of generic fashion accessories
    :param count: Number of accessories to create
    :return: list of accessories
    """
    return [FashionItem(
        "Awesome Accessory {}".format(i+1),
        "Random blurb that no one reads! This is going to be the same",
        "Fake Author #{}".format(i+1),
        "pikachu.png",
        "http://www.youtube.com")
        for i in xrange(count)]


if __name__ == '__main__':
    db.create_all()
    populate_db()