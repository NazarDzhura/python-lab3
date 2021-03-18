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


class Book(RegularItem):

    def __init__(self, name, author, genre, year_of_publication, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.author = author
        self.genre = genre
        self.year_of_publication = year_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Author: {self.author}\n    Genre: {self.genre}\n    Year of publication: " \
               f"{self.year_of_publication}\n    Number of pages: {self.num_of_pages}\n"

    def __del__(self):
        self.__class__.storage.remove(self)


class Comics(RegularItem):
    list_of_items = []

    def __init__(self, name, author, genre, year_of_publication, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.author = author
        self.genre = genre
        self.year_of_publication = year_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Author: {self.author}\n    Genre: {self.genre}\n    Year of publication: " \
               f"{self.year_of_publication}\n    Number of pages: {self.num_of_pages}\n"

    def __del__(self):
        self.__class__.storage.remove(self)


class Magazine(PeriodicalPublishingItem):

    def __init__(self, name, publisher, genre, date_of_publication, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.date_of_publication = date_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Publisher: {self.publisher}\n    Genre: {self.genre}\n" \
               f"    Date of publication: {self.date_of_publication}\n    Number of pages: {self.num_of_pages}\n"

    def __del__(self):
        self.__class__.storage.remove(self)


class Newspaper(PeriodicalPublishingItem):

    def __init__(self, name, publisher, genre, date_of_publication, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.date_of_publication = date_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Publisher: {self.publisher}\n    Genre: {self.genre}\n" \
               f"    Date of publication: {self.date_of_publication}\n    Number of pages: {self.num_of_pages}\n"

    def __del__(self):
        self.__class__.storage.remove(self)


class Journal(PeriodicalPublishingItem):

    def __init__(self, name, publisher, genre, date_of_publication, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.date_of_publication = date_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Publisher: {self.publisher}\n    Genre: {self.genre}\n" \
               f"    Date of publication: {self.date_of_publication}\n    Number of pages: {self.num_of_pages}\n"

    def __del__(self):
        self.__class__.storage.remove(self)

