"""(Incomplete) Tests for BookCollection class."""
from bookcollection import BookCollection
from book import Book
import csv


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    all_books_list = BookCollection()
    print(all_books_list)
    assert not all_books_list.books
    print("Passed")

    # Test loading books
    print("Test loading books:")
    all_books_list.load_books('books.csv')
    print(all_books_list)

    # Test adding a new Book
    print("Test adding new book:")
    all_books_list.add_book(Book("Inspiring Thoughts", "Swami Vivekananda", 107, False))
    print(all_books_list)
    print("passed")

    # Test sorting books
    # TODO: Add more sorting tests

    # TODO: Test get_required_pages()
    # Test required
    print("Test get_required_pages():")
    new_book = BookCollection()
    new_book.add_book(Book("Inspiring Thoughts", "Swami Vivekananda", 107, False))
    assert new_book.get_required_pages() == 107
    assert new_book.get_num_of_required_books() == 1
    print("Passed")

    # TODO: Test saving books (check CSV file manually to see results)

    print("Test saving books:")
    # 5 books sorted by pages
    all_books_list.save_books('collection.csv')
    # 3 books
    new_book.save_books('books.csv')
    print('Passed')

    # TODO: Add more tests, as appropriate


run_tests()
