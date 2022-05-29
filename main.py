"""
Name: Sweta Shree
Date: 28/05/2022
Brief Project Description: This program is for reading tracker.
GitHub URL: https://github.com/cp1404-students/a2-reading-tracker-swetashree2306
"""
# Create your main program in this file, using the ReadingTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


from book import Book


class ReadingTrackerApp(App):

    def __init__(self, **kwargs):
        super().__init__()
        self.filename = None

    def build(self):
        self.title = "Reading Tracker App"
        self.root = Builder.load_file('app.kv')
        return self.root


if __name__ == '__main__':
    ReadingTrackerApp().run()
