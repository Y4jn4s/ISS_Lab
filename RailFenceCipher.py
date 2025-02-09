def rail_fence(text, key, encrypt=True):
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    row, step = 0, 1
    for i, char in enumerate(text):
        rail[row][i] = char
        row += step
        if row == 0 or row == key - 1:
            step *= -1
    result = ''.join([''.join(r) for r in rail]) if encrypt else ''.join(text[i] for r in rail for i, c in enumerate(r) if c)
    return result

def columnar_transposition(text, key, encrypt=True):
    num_cols, num_rows = len(key), -(-len(text) // len(key))
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    sorted_key = sorted(range(len(key)), key=lambda k: key[k])
    if encrypt:
        for i, char in enumerate(text): matrix[i // num_cols][i % num_cols] = char
        return ''.join(matrix[r][c] for c in sorted_key for r in range(num_rows))
    for c, index in enumerate(sorted_key):
        for r in range(num_rows):
            if len(text) > r * num_cols + c:
                matrix[r][index] = text[r * num_cols + c]
    return ''.join(''.join(row) for row in matrix)

def main():
    text, rail_key, col_key = "HELLO WORLD".replace(" ", ""), 3, "31452"
    encrypted = columnar_transposition(rail_fence(text, rail_key), col_key)
    decrypted = rail_fence(columnar_transposition(encrypted, col_key, False), rail_key, False)
    print("Encrypted:", encrypted, "Decrypted:", decrypted)

if __name__ == "__main__":
    main()

"""
Encrypted: LHOEWLLODR 
Decrypted: HELLOWORLD
"""
