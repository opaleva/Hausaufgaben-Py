class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __repr__(self):
        return f'{self.author}: "{self.title}", {self.year}г.\n'


class HomeLibrary:
    def __init__(self, *books: Book):  # * – распаковка кортежа, состоящего из объектов класса Book
        self.books = list(books)

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)

    def search_book(self, **parameters):  # **, т.к. параметры (автор, название, год) именованные
        sought_for = []
        for book in self.books:
            for parameter, value in parameters.items():
                if getattr(book, parameter) != value:
                    break
                else:
                    sought_for.append(book)
        print(*sought_for)

    def sort_author(self, parameter):
        self.books.sort(key=lambda book: getattr(book, parameter))


catalog = HomeLibrary(Book('Marx, Karl', 'Das Kapital', 1867))
catalog.add_book(Book('Ленин, В.И.', 'Государство и революция', 1917))
catalog.add_book(Book(input('Автор: '), input('Название: '),
                      int(input('Год издания (только цифры): '))))

catalog.search_book(author=input('Поиск по автору: '))
catalog.search_book(title=input('Поиск по названию: '))
catalog.remove_book(input('Полное название книги для удаления: '))
catalog.sort_author('author')
print(*catalog.books)
catalog.sort_author('title')
print(*catalog.books)
