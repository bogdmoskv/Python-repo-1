import pytest
from main import add, is_even, reverse_string

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(4) is True

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
