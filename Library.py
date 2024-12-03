class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available == True:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

    def display_info(self):
        print(f"Book info: \ntitle - {self.title}, \nauthor - {self.author}\n")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        [book.display_info() for book in self.books]

    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
            else:
                return None


book1 = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari")
book2 = Book("Mother", "Maxim Gorky")
book3 = Book("Submission to authority", "Stanley Milgram")

books = [book1, book2, book3]
# [book.display_info() for book in books]

library = Library()
for book in books:
    library.add_book(book)

library.display_books()