import csv
from operator import attrgetter
from book import Book


class BookCollection:
    TITLE = "title"
    AUTHOR = "author"
    PAGES = "number_of_pages"
    BACKUP = "backup"

    def __init__(self):
        self.books = []
        self.csv_file = " "

    def __str__(self):
        for book in self.books:
            print(book)
        return ""

    def load_books(self, filename=''):
        """Read csv file and creates list of books."""
        self.filename = filename
        book_file = open(filename, 'r', encoding='utf-8')
        for line in book_file.readlines():
            self.books.append(Book(*line.rstrip().split(',')))
        book_file.close()

    def save_books(self, file_name=" "):
        """Save file in books.csv"""
        with open(file_name, "w", newline="") as csv_file:
            book_list = csv.writer(csv_file)
        for book in self.books:
            book_list.writerow([book.title, book.author, book.number_of_pages, " " if book.is_completed else "*"])

    def add_book(self, book):
        """Add new book in books.csv"""
        self.books.append(book)

    def get_num_of_required_books(self):
        """Get the required number of books."""
        unread_book = 0
        for book in self.books:
            if not book.is_completed:
                unread_book += 1
        return unread_book

    def get_required_pages(self):
        """Get the total number of pages required to read."""
        total_unread_pages = 0
        for book in self.books:
            if not book.is_completed:
                total_unread_pages += book.number_of_pages
        return total_unread_pages

    def string_length(self, attr):
        """Determine length of the books."""
        length = 0
        for book in self.books:
            length_of_title = len(str(getattr(book, attr)))
            if length_of_title > length:
                length = length_of_title
        return length

    def sort(self, key):
        self.books.sort(key=attrgetter(key))
