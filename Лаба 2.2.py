class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        # Используем books=None, чтобы избежать проблемы с мутабельными аргументами по умолчанию
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        # Возвращаем id последней книги + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == "__main__":  # Обратите внимание на два нижних подчеркивания до и после name
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # для пустой библиотеки следующий id должен быть 1

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # следующий id будет равен последнему id + 1 (то есть 3)
    print(library_with_books.get_index_by_book_id(1))  # индекс книги с id = 1 (ожидается 0)
