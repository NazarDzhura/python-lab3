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


class BookstoreManager:
    founded_items = []

    def __init__(self, list_of_items=None) -> None:
        if list_of_items is None:
            list_of_items = []
        self.list_of_items = list_of_items

    def add_item(self, item: BookstoreItem) -> None:
        self.list_of_items.append(item)

    def find_item_by_genre(self, genre) -> list:
        __list_of_suited_items = []
        for item in self.list_of_items:
            if item.genre == genre:
                __list_of_suited_items.append(item)
        self.founded_items = __list_of_suited_items
        return __list_of_suited_items

    def sort_by_name(self, descending=False) -> list:
        __list_of_sorted_items = sorted(self.founded_items, key=lambda item: item.name, reverse=descending)
        return __list_of_sorted_items

    def sort_by_num_of_pages(self, descending=False) -> list:
        __list_of_sorted_items = sorted(self.founded_items, key=lambda item: item.num_of_pages, reverse=descending)
        return __list_of_sorted_items

    def __del__(self) -> None:
        pass


if __name__ == '__main__':
    manager = BookstoreManager(BookstoreItem.storage)
    book1 = Book("Tropic of Cancer", "Henry Miller", "Autobiographical novel", 1934, 318)
    book2 = Book("1984", "George Orwell", "Novel", 1949, 328)
    book3 = Book("Junkie", "William S. Burroughs", "Autobiographical novel", 1953, 166)
    book4 = Book("Edinburgh", "Alexander Chee", "Autobiographical novel", 2001, 209)
    book5 = Book("Giovanni's Room", "James Baldwin", "Poem", 1956, 159)
    book6 = Book("On the Road", "Jack Kerouac", "Autobiographical novel", 1957, 320)

    magazine1 = Magazine("Rolling Stone", "Wenner Media LLC", "Musical", "04.10.2020", 18)
    magazine2 = Magazine("Esquire", "Hearts Communications Inc", "Fashion", "21.11.2014", 22)
    magazine3 = Magazine("Vanity Fair", "Conde Nast", "Musical", "15.12.2020", 30)
    magazine4 = Magazine("Elle", "Kevin OMalley", "Musical", "10.04.2018", 14)

    print("Unsorted list of autobiographical novel genre items:\n")
    for item in manager.find_item_by_genre("Autobiographical novel"):
        print(item)

    print("Sorted by ascending name list of autobiographical novel genre items:\n")
    for item in manager.sort_by_name():
        print(item)

    print("Sorted by descending num of pages list of autobiographical novel genre items:\n")
    for item in manager.sort_by_num_of_pages():
        print(item)