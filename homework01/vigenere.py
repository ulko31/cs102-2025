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
    key_index = 0
    key_len = len(keyword)

    for curr_char in plaintext:
        if curr_char.isalpha():
            shifted_char = shift_char(curr_char, keyword[key_index % key_len], decrypt=False)
            result.append(shifted_char)
            key_index += 1
        else:
            result.append(curr_char)
    return "".join(result)

def decrypt_vigenere(ciphertext, keyword):
    result = []
    key_i = 0
    key_len = len(keyword)

    for c in ciphertext:
        if c.isalpha():
            result.append(shift_char(c, keyword[key_i % key_len], decrypt=True))
            key_i += 1
        else:
            result.append(c)
    return "".join(result)