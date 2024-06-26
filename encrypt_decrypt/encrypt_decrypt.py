# Define the encrypt and decrypt functions
def encrypt(text, key):
    """Encrypt the text using a Caesar cipher with the given key."""
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) + key - offset) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, key):
    """Decrypt the text encrypted using a Caesar cipher with the given key."""
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - key - offset) % 26 + offset)
        else:
            result += char
    return result

# Example usage
plaintext = "Hello,world"
encryption_key = 3

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, encryption_key)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = decrypt(encrypted_text, encryption_key)
print(f"Decrypted text: {decrypted_text}")
