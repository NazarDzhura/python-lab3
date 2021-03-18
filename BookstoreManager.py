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