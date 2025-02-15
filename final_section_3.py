
# # Exercise 1: Library Management System (Encapsulation)
# # --------------------------------------------------
# # Create a Book class that demonstrates proper encapsulation:
# # - Private attributes should include: __title, __author, __isbn, __is_available,
# add your own properties that are not private
# # - Public methods should include: checkout(), return_book(), get_book_info()
# # - Use proper getters and setters
# # - Validate ISBN (must be 13 digits)
# # - Track if book is available for checkout

# # Example usage:
# #     book = Book("Python Programming", "John Smith", "9780123456789")
# #     book.checkout()  # Should mark book as unavailable
# #     book.get_book_info()  # Should return formatted book information___________________________
# # """

def set_isbn(self, isbn):
        if len(isbn) == 13: 
            self.__isbn = isbn
        else:
            raise ValueError("Invalid ISBN. Must be 13 digits.")

def is_available(self):
    return self.__is_available

def checkout(self):
    if self.__is_available:
    self.__is_available = False
    self.due_date = "2024-04-15" 
    else:
    print("Book is already checked out.")
def return_book(self):
    self.__is_available = True
    self.due_date = None
def get_book_info(self):
    availability = "Available" if self.__is_available else "Not Available"
    return f"Title: {self._title}\nAuthor: {self.author}\nISBN: {self._isbn}\nAvailability: {availability}\nDue Date: {self.due_date}"
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
print(book1.get_book_info())
book1.checkout()
print("\nAfter checking out the book:")
print(book1.get_book_info())
book1.checkout()
book1.return_book()
print("\nAfter returning the book:")
print(book1.get_book_info())