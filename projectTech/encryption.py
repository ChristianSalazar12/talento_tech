# This function encrypts a given text using a simple Caesar cipher method.


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


# This function encrypts a given text using the Vigenère cipher method with a specified key
# The key is repeated to match the length of the text, and each letter in the text
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

# This function performs a double encryption on the input text.
# It first applies a Caesar cipher with a specified displacement,
# and then applies a Vigenère cipher using a specified key.
# The result is a text that has been encrypted twice, first with a simple shift and then
# with a more complex key-based method.
# The default key is "123" and the default displacement is 5.
def double_encrypt(text, key="123", desplacement=5):
    first_encrypt = cessar_encrypt(text, desplacement)
    second_encryption = vigenere_encrypt(first_encrypt, key)
    return second_encryption
