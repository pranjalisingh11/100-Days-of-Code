# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and
# show how you can print all books,
# add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.books = []  # list of books
        self.no_of_books = 0    # count of books

    def print_books(self):
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library: ")
            for book in self.books:
                print(book)

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books = len(self.books)

    def get_no_of_books(self):
        return self.no_of_books

my_library = Library()

my_library.add_book("Python Basics")
my_library.add_book("Data Structure")
my_library.add_book("DBMS")

my_library.print_books()

print("Total no. of books: ", my_library.get_no_of_books())
