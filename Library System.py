from abc import ABC, abstractmethod
from datetime import datetime

class Book(ABC):
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.is_available = True

    @abstractmethod
    def display_info(self):
        pass

class FictionBook(Book):
    def display_info(self):
        return f"Fiction Book: {self.title} by {self.author}, Published: {self.publication_date}"

class NonFictionBook(Book):
    def display_info(self):
        return f"Non-Fiction Book: {self.title} by {self.author}, Published: {self.publication_date}"

class Borrower:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.borrowing_history = []

    def borrow_book(self, book):
        if book.is_available:
            borrowing = Borrowing(self, book)
            book.is_available = False
            self.borrowing_history.append(borrowing)
            return borrowing
        else:
            print("Sorry, the selected book is not available for borrowing.")
            return None

    def return_book(self, borrowing):
        borrowing.return_book()
        borrowing.book.is_available = True

class Borrowing:
    def __init__(self, borrower, book):
        self.borrower = borrower
        self.book = book
        self.borrow_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()
        print(f"Book returned by {self.borrower.name}. Borrowed on {self.borrow_date}, Returned on {self.return_date}")


if __name__ == "__main__":

    fiction_book = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10")
    non_fiction_book = NonFictionBook("Sapiens", "Yuval Noah Harari", "2014-02-10")

    borrower = Borrower("Karine", "karine@mail.ru")

    borrowing1 = borrower.borrow_book(fiction_book)
    if borrowing1:
        print(borrowing1.book.display_info())

    borrowing2 = borrower.borrow_book(non_fiction_book)
    if borrowing2:
        print(borrowing2.book.display_info())

    print("\nBorrowing History:")
    for borrowing in borrower.borrowing_history:
        print(f"{borrowing.book.title} by {borrowing.book.author}, Borrowed on {borrowing.borrow_date}")

    borrower.return_book(borrowing1)