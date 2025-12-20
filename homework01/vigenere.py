def shift_char(char, key, decrypt=False):
    if not char.isalpha():
        return char
    char_base = ord('A') if char.isupper() else ord('a')
    key_base = ord('A') if key.isupper() else ord('a')
    char_val = ord(char) - char_base
    key_val = ord(key) - key_base
    if decrypt:
        shifted = (char_val - key_val) % 26
    else:
        shifted = (char_val + key_val) % 26
    return chr(char_base + shifted)

def encrypt_vigenere(plaintext, keyword):
    result = []
    key_len = len(keyword)
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            result.append(shift_char(char, keyword[key_index % key_len], decrypt=False))
            key_index += 1
        else:
            if char == " ":
                key_index += 1
            else:
                key_index = 0
            result.append(char)
    return "".join(result)

def decrypt_vigenere(ciphertext, keyword):
    result = []
    key_len = len(keyword)
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            result.append(shift_char(char, keyword[key_index % key_len], decrypt=True))
            key_index += 1
        else:
            if char == " ":
                key_index += 1
            else:
                key_index = 0
            result.append(char)

    return "".join(result)