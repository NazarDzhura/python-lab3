class BookstoreItem:
    storage = []
    name: str
    genre: str
    num_of_pages: int


class RegularItem(BookstoreItem):
    author: str
    year_of_publication: int


class PeriodicalPublishingItem(BookstoreItem):
    publisher: str
    date_of_publication: str










