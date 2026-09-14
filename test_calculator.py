from calculator import add, subtract, multiply


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(20, 10) == 10


def test_multiply():
    assert multiply(10, 20) == 200