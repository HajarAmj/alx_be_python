class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with a title and author."""
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """Return details about the book."""
        return f"Book: {self.title} by {self.author}"

    def __str__(self) -> str:
        """String representation of the book (same as get_details)"""
        return self.get_details()

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an EBook with title, author, and file size in KB."""
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        """Return details about the ebook including file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __str__(self) -> str:
        """String representation of the ebook"""
        return self.get_details()

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self) -> str:
        """Return details about the print book including page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __str__(self) -> str:
        """String representation of the print book"""
        return self.get_details()

class Library:
    def __init__(self):
        """Initialize a Library to hold a collection of books."""
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self) -> None:
        """Print the details of each book in the library."""
        for book in self.books:
            print(book)
