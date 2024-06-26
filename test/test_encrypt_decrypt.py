import pytest
from encrypt_decrypt.encrypt_decrypt import encrypt, decrypt

def test_encrypt():
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("ABC", 1) == "BCD"
    assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"
    assert encrypt("xyz", 3) == "abc"
    assert encrypt("XYZ", 3) == "ABC"

def test_decrypt():
    assert decrypt("bcd", 1) == "abc"
    assert decrypt("BCD", 1) == "ABC"
    assert decrypt("Khoor, Zruog!", 3) == "Hello, World!"
    assert decrypt("abc", 3) == "xyz"
    assert decrypt("ABC", 3) == "XYZ"

if __name__ == "__main__":
    pytest.main()
