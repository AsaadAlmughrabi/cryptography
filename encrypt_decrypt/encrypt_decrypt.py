def encrypt(input_string, key):
    """
    Encrypts the input string using the Vigenère cipher.
   
    """
    encrypted = ""
    key_length = len(key)
    for i, char in enumerate(input_string):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length].lower()) - ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += shifted_char
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_string, key):
    """
    Decrypts the encrypted string using the Vigenère cipher.
   
    """
    decrypted = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_string):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length].lower()) - ord('a')
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted += shifted_char
        else:
            decrypted += char
    return decrypted

# Example usage:
original_string = "Asaad Almugheabi"
encryption_key = "SECRET"
encrypted_result = encrypt(original_string, encryption_key)
decrypted_result = decrypt(encrypted_result, encryption_key)

print(f"Original: {original_string}")
print(f"Encrypted: {encrypted_result}")
print(f"Decrypted: {decrypted_result}")
