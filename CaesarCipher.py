def encrypt_func(txt, s):
    result = ""

    # Convert the input text to uppercase
    txt = txt.upper()

    # Transverse the plain text
    for i in range(len(txt)):
        char = txt[i]
        # Encrypt uppercase characters in plain text
        if char.isalpha():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += char
    return result

# Check the above function
txt = "CEASER CIPHER EXAMPLE"
s = 4

print("Plain text : " + txt)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt_func(txt, s))

# Solution
Plain txt : CEASER CIPHER EXAMPLE
Shift pattern : 4
Cipher: HJFXJWsHNUMJWsJCFRUQJ
