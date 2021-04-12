import unittest
from Book import *
from Comics import *
from Magazine import *
from Journal import *
from Newspaper import *
from BookstoreManager import *


class TestBookstoreManager(unittest.TestCase):
    # Tests for BookstoreManager.py

    def setUp(self) -> None:
        # setting up testing set of instances

        self.item1 = Book("Tropic of Cancer", "Henry Miller", "Autobiographical novel", 1934, 318)
        self.item2 = Book("1984", "George Orwell", "Novel", 1949, 328)
        self.item3 = Book("Junkie", "William S. Burroughs", "Autobiographical novel", 1953, 166)
        self.item4 = Book("On the Road", "Jack Kerouac", "Autobiographical novel", 1957, 320)
        self.item5 = Comics("Deadpool", "Marvel", "Superhero", 2019, 25)
        self.item6 = Journal("ATT", "AT", "Celebrity", "10.20.2021", 14)
        self.item7 = Newspaper("NYT", "NY", "Weekly", "04.10.2020", 20)
        self.item8 = Magazine("Rolling Stone", "Wenner Media LLC", "Musical", "04.10.2020", 18)
        result = [self.item1, self.item2, self.item3, self.item4, self.item5, self.item6, self.item7]
        self.manager = BookstoreManager(result)

    def test_find_item_by_genre(self) -> None:
        # 'find_item_by_genre' should return only suitable items

        self.assertEqual(self.manager.find_item_by_genre("Autobiographical novel"),
                         [self.item1, self.item3, self.item4])

    def test_sort_by_name_ascending(self) -> None:
        # 'sort_by_name' should sort list of founded items by name ascending

        self.manager.founded_items = self.manager.find_item_by_genre("Autobiographical novel")
        self.assertEqual(self.manager.sort_by_name(), [self.item3, self.item4, self.item1])

    def test_sort_by_name_descending(self) -> None:
        # 'sort_by_name' should sort list of founded items by name descending

        self.manager.founded_items = self.manager.find_item_by_genre("Autobiographical novel")
        self.assertEqual(self.manager.sort_by_name(descending=True), [self.item1, self.item4, self.item3])

    def test_sort_by_num_of_pages_ascending(self) -> None:
        # 'sort_by_num_of_pages' should sort list of founded items by number of pages ascending
        self.manager.founded_items = self.manager.find_item_by_genre("Autobiographical novel")
        self.assertEqual(self.manager.sort_by_num_of_pages(), [self.item3, self.item1, self.item4])

    def test_sort_by_num_of_pages_descending(self) -> None:
        # 'sort_by_num_of_pages' should sort list of founded items by number of pages descending
        self.manager.founded_items = self.manager.find_item_by_genre("Autobiographical novel")
        self.assertEqual(self.manager.sort_by_num_of_pages(descending=True), [self.item4, self.item1, self.item3])


if __name__ == "__main__":
    unittest.main()
