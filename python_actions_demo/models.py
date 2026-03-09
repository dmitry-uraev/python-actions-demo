class Book:
    """Book model"""
    def __init__(self, id: int, title: str, price: float):
        self.id = id
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f"{self.title} (${self.price})"

    def increase_price(self, amount: float):
        self.price += amount

class Library:
    """Library model"""
    def __init__(self, name: str):
        self.name = name
        self.books = {}

    def add_book(self, book):
        if book.id in self.books:
            raise ValueError("Book ID exists")
        self.books[book.id] = book

    def remove_book(self, book_id):
        self.books.pop(book_id, None)

    def get_book(self, book_id):
        return self.books.get(book_id)
