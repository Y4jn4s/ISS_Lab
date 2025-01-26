def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, mod):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible.")
    return [[matrix[1][1] * det_inv % mod, -matrix[0][1] * det_inv % mod],
            [-matrix[1][0] * det_inv % mod, matrix[0][0] * det_inv % mod]]

def hill_encrypt(message, key):
    while len(message) % 2 != 0:
        message += 'X'
    message_vector = [ord(c) - ord('A') for c in message.upper()]
    encrypted = ""
    for i in range(0, len(message_vector), 2):
        x, y = message_vector[i], message_vector[i + 1]
        encrypted += chr((key[0][0] * x + key[0][1] * y) % 26 + ord('A'))
        encrypted += chr((key[1][0] * x + key[1][1] * y) % 26 + ord('A'))
    return encrypted

def hill_decrypt(encrypted, key):
    key_inv = matrix_mod_inverse(key, 26)
    encrypted_vector = [ord(c) - ord('A') for c in encrypted]
    decrypted = ""
    for i in range(0, len(encrypted_vector), 2):
        x, y = encrypted_vector[i], encrypted_vector[i + 1]
        decrypted += chr((key_inv[0][0] * x + key_inv[0][1] * y) % 26 + ord('A'))
        decrypted += chr((key_inv[1][0] * x + key_inv[1][1] * y) % 26 + ord('A'))
    return decrypted.rstrip('X')

key = [[6, 24], [1, 13]]
plaintext = "HELLO"
encrypted = hill_encrypt(plaintext, key)
print(f"Encrypted Message: {encrypted}")
decrypted = hill_decrypt(encrypted, key)
print(f"Decrypted Message: {decrypted}")

''' For the key matrix [[6, 24], [1, 13]]:

Input: "HELLO"
Encrypted: "ZEBBWX"
Decrypted: "HELLO"
'''
