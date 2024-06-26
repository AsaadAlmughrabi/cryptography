# tests/test_encrypt_decrypt.py

import pytest
from encrypt_decrypt.encrypt_decrypt import encrypt, decrypt



def test_encrypt_decrypt():
    original_string = "Hello, World!"
    encryption_key = "SECRET"


    encrypted_result = encrypt(original_string, encryption_key)

    
    decrypted_result = decrypt(encrypted_result, encryption_key)

    
    assert decrypted_result == original_string, "Decryption failed"

if __name__ == "__main__":
    pytest.main()