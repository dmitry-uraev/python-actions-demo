import pytest

from python_actions_demo.models import Book, Library


# test add book to library
def test_lib_add_book(book_python):
    lib = Library("Test Library")
    lib.add_book(book_python)
    assert lib.get_book(1) is book_python


# check error raises for duplicate book
def test_lib_error_duplicate_book(book_python):
    lib = Library("Test Library")
    lib.add_book(book_python)
    dup_book = Book(1, "Duplicate", 100.0)
    with pytest.raises(ValueError):
        lib.add_book(dup_book)


# check book remove
def test_lib_remove_book(book_python):
    lib = Library("Test Library")
    lib.add_book(book_python)
    lib.remove_book(1)
    assert lib.get_book(1) is None
