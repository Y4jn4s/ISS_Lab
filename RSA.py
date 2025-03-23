import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys():
    p, q = 61, 53  # Prime numbers
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.choice([3, 5, 17, 257, 65537])  # Common public exponents

    while gcd(e, phi) != 1:
        e += 2  # Find a coprime

    d = mod_inverse(e, phi)
    return (e, n), (d, n)  # Public, Private keys

def rsa_encrypt(text, pub_key):
    e, n = pub_key
    return [pow(ord(c), e, n) for c in text]

def rsa_decrypt(cipher, priv_key):
    d, n = priv_key
    return "".join(chr(pow(c, d, n)) for c in cipher)

public_key, private_key = generate_keys()
text = "RSA"

encrypted = rsa_encrypt(text, public_key)
decrypted = rsa_decrypt(encrypted, private_key)

print("RSA Encrypted:", encrypted)
print("RSA Decrypted:", decrypted)
