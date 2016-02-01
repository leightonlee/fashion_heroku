from ..apps import app


class FashionItem(app.db.Model):
    __tablename__ = 'FashionItem'
    id = app.db.Column(app.db.Integer, primary_key=True, autoincrement=True)
    title = app.db.Column(app.db.String(200))
    blurb = app.db.Column(app.db.String(1000))
    author = app.db.Column(app.db.String(200))
    thumbnail_url = app.db.Column(app.db.String(200))
    details_url = app.db.Column(app.db.String(200))

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
