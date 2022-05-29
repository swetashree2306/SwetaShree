"""
Name: Sweta Shree
Date: 28/05/2022
Brief Project Description: This program is for reading tracker.
GitHub URL: https://github.com/cp1404-students/a2-reading-tracker-swetashree2306
"""
# Create your main program in this file, using the ReadingTrackerApp class
from kivy import key
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

from bookcollection import BookCollection
from book import Book


class ReadingTrackerApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.book_collection = BookCollection()
        self.filename = []

    def build(self):
        self.title = "Reading Tracker App 2.0"
        self.root = Builder.load_file('app.kv')
        self.print_books()
        self.get_required_pages()
        self.sort_list("title")
        return self.root

    def on_start(self):
        self.book_collection.load_books("movies.csv")
        self.print_book()
        self.get_required_pages()
        self.sort_list("title")

    def get_required_pages(self):
        pass

    def sort_list(self, title):
        pass

    def print_book(self):
        pass


if __name__ == '__main__':
    ReadingTrackerApp().run()
