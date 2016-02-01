from fashion_items import FashionItem


class FashionStore():
    def __init__(self, app):
        self.app = app

    def get_fashion_items(self, page, items_per_page):
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

    def create_fashion_item(self, fasion_item):
        try:
            self.app.db.session.add(fasion_item)
            self.app.db.session.commit()
        except Exception:
            self.app.db.session.rollback()


def create_fashion_store(app):
    app.fashion_store = FashionStore(app)