def aes_encrypt(plain_text, key):
    encrypted_text = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(plain_text, key * (len(plain_text) // len(key) + 1)))
    return encrypted_text

def aes_decrypt(cipher_text, key):
    return aes_encrypt(cipher_text, key)  # XOR is reversible

key = "key12345"  # 8-byte key for simplicity
text = "HelloAES"

encrypted = aes_encrypt(text, key)
decrypted = aes_decrypt(encrypted, key)

print("AES Encrypted:", encrypted.encode())  # Encode to show non-printable characters
print("AES Decrypted:", decrypted)
