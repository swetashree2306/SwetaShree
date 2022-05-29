
"""Implements the Book class containing the title, author, and page count."""
# Create your Book class in this file


class Book:
    """Implements the Book class."""

    def __init__(self, title="", author="", number_of_pages=0, is_completed=False):

        self.title = title

        self.author = author

        self.number_of_pages = int(number_of_pages)

        self.is_completed = is_completed

    def __str__(self):
        return "{}, {}, {} pages, required: {}".format(self.title, self.author, self.number_of_pages,  self.is_completed)

    def str_to_csv(self):
        """ Mark the books in CVS."""
        return ','.join((self.title, self.author, str(self.number_of_pages), 'c' if self.is_completed else 'r'))

    def mark_required(self):
        """Mark the book if it is required."""
        self.is_completed = False

    def mark_completed(self):
        """Mark the book if it is completed."""
        self.is_completed = True

    def is_long(self):
        """Check Book length."""
        return self.number_of_pages > 500
