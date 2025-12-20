def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            ciphertext += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            ciphertext += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            plaintext += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            plaintext += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += ch
    return plaintext