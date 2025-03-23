def xor(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def feistel_round(left, right, key):
    new_right = xor(left, key)
    return right, new_right  # Swap

def des_encrypt(plain_text, key, rounds=4):  # Simplified with fewer rounds
    binary_text = "".join(format(ord(c), '08b') for c in plain_text).ljust(16, '0')
    left, right = binary_text[:8], binary_text[8:]
    
    for _ in range(rounds):
        left, right = feistel_round(left, right, key)
    
    return left + right

def des_decrypt(cipher_text, key, rounds=4):
    left, right = cipher_text[:8], cipher_text[8:]

    for _ in range(rounds):
        right, left = feistel_round(right, left, key)  # Reverse process
    
    return "".join(chr(int(left[i:i+8], 2)) for i in range(0, len(left), 8))

key = "11001010"  # 8-bit key for simplicity
text = "HI"
encrypted = des_encrypt(text, key)
decrypted = des_decrypt(encrypted, key)

print("DES Encrypted:", encrypted)
print("DES Decrypted:", decrypted)
