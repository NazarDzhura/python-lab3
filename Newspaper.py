from BookstoreItem import *


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