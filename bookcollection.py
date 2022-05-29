import operator
from book import Book


class BookCollection:
    TITLE = "title"
    AUTHOR = "author"
    PAGES = "number_of_pages"
    BACKUP = "backup"

    def __init__(self):
        self.file_name = None
        self.books = []
        self.csv_file = " "

    def __str__(self):
        """List command implementation."""
        marking = ''
        for number, book in enumerate(self.books, start=1):
            marking += ('{0}{1}. {2:<{5}} by {3:<{6}}  {4:>{7}} page{8}\n'.format(' ' if book.is_completed else '*',
                                                                                  number, book.title, book.author,
                                                                                  book.number_of_pages,
                                                                                  self.string_length(
                                                                                      BookCollection.TITLE),
                                                                                  self.string_length(
                                                                                      BookCollection.AUTHOR),
                                                                                  self.string_length(
                                                                                      BookCollection.PAGES),
                                                                                  '' if book.number_of_pages == 1 else
                                                                                  's '))
            # marking += ("{}, {}, {} pages, {}\n".format(' ' if book.is_completed else '*', number, book.title,
            #                                                     book.author, book.number_of_pages,  book.is_completed))
        if marking:
            required = (
                'You need to read {0} pages in {1} books.'.format(self.get_required_pages(),
                                                                  self.get_num_of_required_books()))
            return marking + required
        else:
            return 'Currently no book available.'

    # def save_books(self, csv_file=''):
    #     """Save csv file for list of books."""
    #
    # csv_file = "books.csv" or self.csv_file
    # file = open(csv_file, "w")
    # for book in self.books:
    #     print(book.str_to_csv(), file=file)
    #
    # file.close()

    def load_books(self, csv_file=''):
        """Read csv file and creates list of books."""
        self.filename = csv_file
        file_book = open(csv_file, 'r+')
        for line in file_book.readlines():
            self.books.append(Book(*line.rstrip().split(',')))
        file_book.close()

    def save_books(self, csv_file=" "):
        """Save file in books.csv"""
        csv_file = "books.csv" or self.csv_file
        book_list = open(csv_file, 'r+')
        for book in self.books:
            print(book.str_to_csv(), file=book_list)
        book_list.close()

    def add_book(self, book):
        """Add new book in books.csv"""
        self.books.append(book)

    def get_num_of_required_books(self):
        """Get the required number of books."""
        number_of_books = 0
        for book in self.books:
            if not book.is_completed:
                number_of_books += 1
        return number_of_books

    def get_required_pages(self):
        """Get the total number of pages required to read."""
        total_pages = 0
        for book in self.books:
            if not book.is_completed:
                total_pages += book.number_of_pages
        return total_pages

    def string_length(self, attr):
        """Determine length of the books."""
        length = 0
        for book in self.books:
            length_of_title = len(str(getattr(book, attr)))
            if length_of_title > length:
                length = length_of_title
        return length
