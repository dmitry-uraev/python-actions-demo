import pytest

from src.models import Library
from src.models import Book


@pytest.fixture
def book_python() -> Book:
    return Book(1, "Fluent Python", 25.)

@pytest.fixture
def book_js() -> Book:
    return Book(2, "JavaScript Basics", 20.)

@pytest.fixture
def library_one_book(book_python) -> Library:
    lib = Library("Test Library")
    lib.add_book(book_python)
    return lib

@pytest.fixture
def catalog_two_libs(book_python, book_js) -> dict[str, Library]:
    libA = Library("Library A")
    libA.add_book(book_python)

    libB = Library("Library B")
    libB.add_book(book_js)

    return {
        "lib1": libA,
        "lib2": libB
    }
