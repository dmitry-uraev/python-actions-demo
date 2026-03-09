import pytest
from src.models import Book

@pytest.mark.parametrize("start_price,increase,expected", [
    (25.0, 5.0, 30.0),
    (30.0, 0.0, 30.0),
    (20.0, 10.0, 30.0),
])
@pytest.mark.book
def test_book_price_increase(start_price, increase, expected):
    book = Book(id=99, title="Test", price=start_price)
    book.increase_price(increase)
    assert book.price == expected
