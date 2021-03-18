from BookstoreItem import BookstoreItem, Book, Magazine
from BookstoreManager import BookstoreManager

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

    print("Sorted by descending num of pages list of autobiographical novel genre items:\n", True)
    for item in manager.sort_by_num_of_pages():
        print(item)