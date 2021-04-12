from BookstoreItem import *


class Comics(RegularItem):

    def __init__(self, name: str, author: str, genre: str, year_of_publication: int, num_of_pages: int = 1) -> None:
        self.__class__.storage.append(self)
        self.name = name
        self.author = author
        self.genre = genre
        self.year_of_publication = year_of_publication
        self.num_of_pages = num_of_pages

    def __str__(self) -> str:
        return f"    Name: {self.name}\n    Author: {self.author}\n    Genre: {self.genre}\n    Year of publication: " \
               f"{self.year_of_publication}\n    Number of pages: {self.num_of_pages}\n"
