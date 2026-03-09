from src.models import Book

# step 1. simple test
def test_book_info():
    book = Book(1, "Fluent Python", 25.).get_info()
    assert "Fluent Python" in book
    assert "$25.0" in book

# step 2. simple test, but again book creation is duplicated
def test_book_price_increase():
    book = Book(id=99, title="Test", price=25.)
    book.increase_price(5.)
    assert book.price == 30.
