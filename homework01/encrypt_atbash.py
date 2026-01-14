def encrypt_atbash(plaintext: str) -> str:
    result = []
    for ch in plaintext:
        if "a" <= ch <= "z":
            result.append(chr(ord("a") + (ord("z") - ord(ch))))
        elif "A" <= ch <= "Z":
            result.append(chr(ord("A") + (ord("Z") - ord(ch))))
        else:
            result.append(ch)
    return "".join(result)

if __name__ == "__main__":
    print(encrypt_atbash("Hello, World!"))
    print(encrypt_atbash("abcXYZ"))
