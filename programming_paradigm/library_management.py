class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def __repr__(self):
        return f"{self.title} by {self.author}"
    def return_book(self):
        self._is_checked_out = False
    
    def check_out_book(self):
        self._is_checked_out = True
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book:Book):
        self._books.append(book)
    
    def check_out_book(self, title):
        book:Book = [x for x in self._books if x.title == title][0]
        book._is_checked_out = True
    
    def return_book(self, title):
        book:Book = [x for x in self._books if x.title == title][0]
        book._is_checked_out = False
    
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(book)
