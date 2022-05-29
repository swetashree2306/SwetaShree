"""..."""
# Copy your first assignment to this file, then update it to use Book class
# Optionally, you may also use BookCollection class

# from book import Book

"""
CP1404- Assignment-01
Name- Sweta Shree
Student Code- 13911865

"""

import csv

class Assign_1:

    lists = []


    def menu(self):
        global choice
        print("Reading Tracker 1.0 - by Lindsay Ward\n 4 books loaded")
        print("Menu: \n L - List all books\n A - Add new book \n M - Mark a book as completed\n Q - Quit")


    menu()
    choice = input("Choose an option from menu: ").upper()


    def list_book(self):
        global file, csv_reader, line
        file = open("books.csv")
        for line in file:
            print(line)


    while choice != "Q":
        if choice == "L":
            list_book()

        elif choice == "A":
            if choice == "L":
                file = open("books.csv", "r+")
                csv_reader = csv.reader(file)
                for line in csv_reader:
                    print(line)

            elif choice == "A":
                title = input("Title:")
                while title == "":
                    print("Input can not be blank")
                    title = input("Title:")

                author = input("Author:")
                while author == "":
                    print("Input can not be blank")
                    author = input("Author:")

                pages = int(input("Pages:"))
                while pages == "":
                    print("Input can not be blank")
                    pages = int(input("Pages:"))
                while pages < 0:
                    print("Number must be > 0")
                    pages = int(input("Pages:"))

                print("{0} by {1}, ({2}) added to Reading Tracker".format(title, author, pages))

                new_line = [title, author, pages]
                file = open("books.csv", 'a+')
                csv_writer = csv.writer(file)
                csv_writer.writerow(new_line)
                file.close()

        elif choice == "M":
            file = open('books.csv', 'r')
            csv_reader = csv.reader(file)
            for line in csv_reader:
                all_books = [line]
                title = csv.reader(file)
                mark_book = int(input("Enter the number of a book to mark as completed:"))
                if mark_book < 1:
                    print("Invalid input; enter a valid number")
                    mark_book = int(input("Enter the number of a book to mark as completed:"))

        else:
            print("Invalid menu choice")

        print()
        menu()
        choice = input("Choose an option from menu: ").upper()

    print("thank you")


