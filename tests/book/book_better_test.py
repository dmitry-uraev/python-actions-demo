# step 3. simple test with fixture
def test_book_info(book_python):
    assert "Fluent Python" in book_python.get_info()
    assert "$25.0" in book_python.get_info()


# step 2. simple test, withiout duplication
def test_book_price_increase(book_js):
    book_js.increase_price(5.0)
    assert book_js.price == 25.0
