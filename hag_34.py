class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __repr__(self):
        return f'{self.author}: "{self.title}", {self.year}г.'


class Librarian:
    def __init__(self, *books: Book):
        self.books = list(books)
        self.borrowed_books = list(books)

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга {book} удалена.\n")

    def return_book(self, return_book):
        for book in self.borrowed_books:
            if return_book == book.title.lower():
                self.books.append(book)
                self.borrowed_books.remove(book)
                print(f"Книга {book} возвращена.\n")

    def lend_book(self, get_book):
        for book in self.books:
            if get_book == book.title.lower():
                self.borrowed_books.append(book)
                self.books.remove(book)
                print(f"Книга {book} взята.\n")

    def display_books(self):
        for book in self.books:
            print(book)


class Reader:
    def __init__(self):
        self.book = Book(author=None, title=None, year=None)

    def get_book(self):
        self.book.title = input("Название книги: ")
        return self.book.title.lower()

    def return_book(self):
        self.book.title = input("Название книги: ")
        return self.book.title.lower()


class LibraryFacade:
    def __init__(self):
        self.librarian = Librarian()
        self.reader = Reader()

    def add_book(self, book):
        self.librarian.add_book(book)

    def remove_book(self, title):
        self.librarian.remove_book(title)

    def display_books(self):
        self.librarian.display_books()

    def get_book(self):
        self.librarian.lend_book(self.reader.get_book())

    def return_book(self):
        self.librarian.return_book(self.reader.return_book())


def main():
    catalog = LibraryFacade()
    catalog.add_book(Book('Marx, Karl', 'Das Kapital', 1867))
    catalog.add_book(Book('Ленин, В.И.', 'Государство и революция', 1917))
    catalog.add_book(Book('Kim Il Sung', 'Episoden aus dem Leben', 2007))

    while True:
        question = input("Что делать будем?\n1 — Смотреть все книги\n2 — Взять книгу\n"
                         "3 — Вернуть книгу\n4 – Добавить книгу\n5 — Удалить книгу\nЧто-либо другое – Выйти")
        if question == "1":
            catalog.display_books()
        elif question == "2":
            catalog.get_book()
        elif question == "3":
            catalog.return_book()
        elif question == "4":
            catalog.add_book(Book(input('Автор: '), input('Название: '), int(input('Год издания (только цифры): '))))
        elif question == "5":
            catalog.remove_book(input('Полное название книги для удаления: '))
        else:
            break


if __name__ == '__main__':
    main()
