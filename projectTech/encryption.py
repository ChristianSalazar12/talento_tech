def cessar_encrypt(text, displacement=5):
    answer = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            answer += chr((ord(char) - base + displacement) % 26 + base)
        elif char.isdigit():
            answer += str((int(char) + displacement) % 10)
        else:
            answer += char
    return answer


def vigenere_encrypt(text, key):
    answer = ""
    repeted_key = (key * ((len(text) // len(key)) + 1))[: len(text)]

    for i, char in enumerate(text):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            key_char = repeted_key[i].lower()
            displacement = ord(key_char) - ord("a")
            answer += chr((ord(char) - base + displacement) % 26 + base)

        else:
            answer += char
    return answer


def double_encrypt(text, key="123", desplacement=5):
    first_encrypt = cessar_encrypt(text, desplacement)
    second_encryption = vigenere_encrypt(first_encrypt, key)
    return second_encryption
